#!/usr/bin/env python3
"""Kiem tra thu tu \\bibitem trong references.tex co khop voi thu tu
xuat hien lan dau cua tung khoa trich dan (\\citep/\\citet/\\cite...) khi
doc theo dung thu tu \\input trong main.tex hay khong.

Chay:
    python scripts/check_citation_order.py

Thoat voi ma 0 neu khop hoan toan, ma 1 neu co sai lech (in danh sach
lech ra stdout). Dung nhu buoc nghiem thu bat buoc sau moi WP co sua
noi dung trich dan.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INPUT_RE = re.compile(r'^\s*\\input\{([^}]+)\}')
# \cite, \citep, \citet, \citeauthor, \citeyear... with optional [..][..] locators
CITE_RE = re.compile(r'\\cite[a-zA-Z]*(?:\[[^\]]*\])*\{([^}]+)\}')
BIBITEM_RE = re.compile(r'\\bibitem\{([^}]+)\}')
COMMENT_STRIP_RE = re.compile(r'(?<!\\)%.*')


def strip_comments(line: str) -> str:
    return COMMENT_STRIP_RE.sub('', line)


def get_input_order(main_tex: Path):
    files = []
    for raw in main_tex.read_text(encoding='utf-8').splitlines():
        line = strip_comments(raw)
        m = INPUT_RE.match(line)
        if m:
            name = m.group(1)
            if not name.endswith('.tex'):
                name = name + '.tex'
            files.append(name)
    return files


def get_citation_order(tex_files):
    """Return list of citation keys in first-appearance order across files,
    reading each file top to bottom (floats use [H] so source order ==
    render order)."""
    seen = []
    seen_set = set()
    for fname in tex_files:
        path = ROOT / fname
        if not path.exists():
            continue
        text = '\n'.join(strip_comments(l) for l in path.read_text(encoding='utf-8').splitlines())
        for m in CITE_RE.finditer(text):
            keys = [k.strip() for k in m.group(1).split(',')]
            for k in keys:
                if k and k not in seen_set:
                    seen_set.add(k)
                    seen.append(k)
    return seen


def get_bibitem_order(references_tex: Path):
    text = '\n'.join(strip_comments(l) for l in references_tex.read_text(encoding='utf-8').splitlines())
    return [m.group(1) for m in BIBITEM_RE.finditer(text)]


def main():
    main_tex = ROOT / 'main.tex'
    references_tex = ROOT / 'references.tex'

    body_files = [f for f in get_input_order(main_tex) if f != 'references.tex']
    citation_order = get_citation_order(body_files)
    bibitem_order = get_bibitem_order(references_tex)

    ok = True

    cited_not_in_bib = [k for k in citation_order if k not in bibitem_order]
    bib_not_cited = [k for k in bibitem_order if k not in citation_order]
    if cited_not_in_bib:
        ok = False
        print(f"[LOI] {len(cited_not_in_bib)} khoa duoc \\cite nhung khong co \\bibitem:")
        for k in cited_not_in_bib:
            print(f"  - {k}")
    if bib_not_cited:
        ok = False
        print(f"[LOI] {len(bib_not_cited)} \\bibitem khong duoc \\cite o dau trong than bai:")
        for k in bib_not_cited:
            print(f"  - {k}")

    common_citation_order = [k for k in citation_order if k in bibitem_order]
    n = len(common_citation_order)
    matches = 0
    mismatches = []
    for i, key in enumerate(common_citation_order):
        expected = bibitem_order[i] if i < len(bibitem_order) else None
        if expected == key:
            matches += 1
        else:
            mismatches.append((i + 1, key, expected))

    print(f"Khop thu tu: {matches}/{n}")
    if mismatches:
        ok = False
        print("Cac vi tri lech (vi tri, khoa trich dan lan dau theo than bai, khoa dang co trong bibitem cung vi tri):")
        for pos, cited_key, bib_key in mismatches:
            print(f"  {pos}: than bai='{cited_key}'  bibitem='{bib_key}'")

    if ok:
        print("KET QUA: thu tu bibitem khop hoan toan voi thu tu trich dan lan dau.")
    else:
        print("KET QUA: CO SAI LECH. Sua references.tex cho khop thu tu that su trong than bai.")

    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
