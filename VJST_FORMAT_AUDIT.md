# VJST format/reference audit — WP7.6

Audit date: 09/08/2026.

## Current VJST-MOST requirements checked

The current VJST-MOST author guidance requires numbered in-text references in square brackets and a final reference list written in English and numbered by order of first appearance. For references with more than three authors, the first three authors are listed followed by `et al.`. The guidance asks authors to provide DOI, URL and access date when available/relevant. The current submission checklist asks for OpenOffice/Microsoft Word/RTF, 12-point single-spaced text, with figures/tables placed in the text.

Sources checked:
- https://b.vjst.vn/index.php/ban_b/quy-dinh-bai-viet
- https://b.vjst.vn/index.php/ban_b/about/submissions

## Reference audit

- Citation keys used in article: **35**.
- `\\bibitem` entries: **35**.
- Missing references: **0**.
- Unused references: **0**.
- Order of `\\bibitem` vs first citation: **exact match**.
- Entries with >3 authors have been normalized to first three authors + `et al.`.
- Stable official URLs/access date 9 August 2026 were added where verified for the principal Vietnamese laws/decrees/decisions and major online standards/guidance.
- The accepted prior article remains marked `accepted for publication`; no DOI is invented.

## Manuscript-format status

- QA PDF after WP7.6: **29 pages**.
- Abstracts: **249 Vietnamese words / 210 English words**.
- XeLaTeX: no undefined citation/reference and no overfull box; only a harmless hyperref empty-anchor warning remains.

The TeX/PDF file is a **QA manuscript**, retaining typography close to the editorially processed `4044_VJST.docx` for continuity. It is not the final upload file. The final submission version should be produced as DOCX and reconciled to the current OJS checklist (12 pt, single spacing) without altering content, numbering, captions, citations or figures.

## Architecture/claim status after WP7.6

- Main architecture term: province–central distributed reference architecture / kiến trúc tham chiếu phân tán tỉnh–trung ương.
- V1–V6 each has an explicit artefact; deployment is separated from static container structure.
- 128 atomic source constraints / 116 source units remain unchanged.
- Scenario result remains 2 direct + 7 conditional + 1 architectural risk; no ranking that asserts general superiority of B1.
- Future validation in the manuscript is limited to objective evidence from a prototype and repeatable tests: interoperability, transfer of write authority, rolling upgrade/schema compatibility, recovery, security and quality attributes.

## Remaining submission tasks

1. Build the final DOCX using the VJST/OJS typography and inline-figure requirements.
2. Perform a final visual check after DOCX conversion because pagination/table wrapping will change from the QA PDF.
3. Recheck the status of the draft specialised-data standard immediately before submission; if it becomes official, reclassify D rows and rerun traceability.
