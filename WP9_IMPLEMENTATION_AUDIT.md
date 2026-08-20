# WP9 implementation audit

Date: 2026-08-10

## Result by work package

- WP9.1: separated the conformance core of the SRA from deployment profile P-DIST. Physical per-province storage is an L2 profile choice, not a legal requirement or a universal optimum.
- WP9.2: added CR1--CR9 for core conformance and PD1--PD2 for P-DIST conformance.
- WP9.3: refined S9 with `write_scope`, monotonic `writer_epoch`, stale-writer fencing, in-flight-case handling, and the transfer state machine `prepared -> old-frozen -> cutover-confirmed -> new-active -> completed`. Re-ran S1--S10 on B1-R/P-DIST.
- WP9.4: reconciled the evidence chain to 16 corpus documents, 116 source units, and 128 traceability rows (114 A, 8 D, 6 M). Class-A design-response status is 110 satisfied, 3 partial, and 1 requiring clarification. Added release placeholders for URL, tag, commit, and checksum.
- WP9.5: added an explicit delta matrix against the prior study and kept it outside the synthesis corpus. The original 14-token n-gram audit used editorial manuscript `4044_VJST.docx`; no substantive overlap was found, with matches limited to author affiliations and addresses. The citation source is now the final published `JSTPM_paper.pdf`.
- WP9.6: consolidated the pre/post-refinement evaluation table, removed repeated novelty-defence prose, fixed layout overflow, and refreshed the prior-work citation from accepted-manuscript metadata to the final JSTPM publication (Vol. 15, No. 2, 2026, pp. 45--68). In-text locators were changed to published pages 54 and 58--59, and internal label `4044` was removed from manuscript-facing prose/table labels before the final rebuild and visual QA.

## Machine-readable checks

| Artifact | Check |
|---|---:|
| `corpus_manifest.csv` | 16 records |
| `source_unit_index.csv` | 116 records |
| `constraint_traceability.csv` | 128 records |
| source classes | A=114; D=8; M=6 |
| class-A status | satisfied=110; partial=3; clarification=1 |
| `conformance_rules.csv` | 9 core rules + 2 P-DIST rules |
| `evaluation_results_b1r.csv` | 10 scenarios |
| B1-R/P-DIST result | direct=2; conditional=8; unabsorbed L2 architecture risk=0 |

## Build and visual QA

- Build command: `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`.
- Output: 41 A4 pages.
- No overfull boxes, undefined citations, or undefined cross-references in the final log.
- Pages containing the prior-work delta table, conformance table, architecture figures, and B1-R evaluation table were rendered to PNG and visually inspected.
- Times New Roman is unavailable in the current build environment. `main.tex` therefore falls back to DejaVu Serif for QA only; the submission DOCX must still use Times New Roman according to the project formatting rule.

## Pre-submission items deliberately left open

- Replace `[URL]`, `[TAG]`, `[COMMIT]`, and `[CHECKSUM]` with a read-only evidence release.
- Implement a prototype and execute concurrency, cutover, restart, forward-recovery, rolling-upgrade, and compatibility tests. The current 2/8/0 result is a design-level post-check, not operational proof.
- Regenerate and visually verify the DOCX submission file using Times New Roman. The existing `VJST2_submission_ready.docx` has not been overwritten by WP9 because an automatic LaTeX-to-DOCX conversion would not preserve the verified TikZ figures and journal layout reliably.
