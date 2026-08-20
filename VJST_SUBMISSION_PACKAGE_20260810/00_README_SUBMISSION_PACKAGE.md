# VJST Submission Package — 10/08/2026

## 01_UPLOAD_TO_OJS
Upload by default:
1. `01_MANUSCRIPT_VJST2_round5_hardened.docx` — main manuscript.
2. `02_SUPPLEMENTARY_MATERIAL.pdf` — supplementary material referenced by the manuscript.

Do not upload the detached figure files by default because the current VJST checklist requires figures/tables inline in the manuscript. Use folder `03_FIGURE_SOURCES_IF_REQUESTED` only if the editor requests separate figure files.

## 02_SUPPLEMENTARY_DATA_RELEASE
Machine-readable research artefacts supporting traceability and scenario-based architecture evaluation. This directory is intended as the frozen supplementary-data release if the submission/editor allows or requests an external data package.

Core contents include corpus/source indexes, traceability matrix, atomization rules, architecture drivers/decisions/elements/variation/conformance registries, scenario/rubric/coverage files, before/after evaluation results and the architecture refinement log.

Before citing this directory as evidence, freeze its contents and change sharing permission to read-only/viewer. Record the snapshot date/version and, if desired, a checksum manifest.

## 03_FIGURE_SOURCES_IF_REQUESTED
Five PNG files extracted directly from the current Round-5 DOCX, so they match the submitted manuscript. These are not intended as default OJS upload files unless the editorial office requests detached artwork.

## 99_INTERNAL_DO_NOT_UPLOAD
Internal format/consistency audits. Do not submit these files as manuscript attachments.

## Current official VJST checklist checked 10/08/2026
- Submission file: OpenOffice, Microsoft Word or RTF.
- Text: 12-point, single-spaced.
- Figures and tables: placed inline at the appropriate points in the manuscript.
- References: numbered in square brackets in first-appearance order; final reference list in English; include DOI/URL/access date when applicable.

Official pages:
- https://b.vjst.vn/index.php/ban_b/about/submissions
- https://b.vjst.vn/index.php/ban_b/quy-dinh-bai-viet

## Final pre-upload checks
1. Resolve the known typography conflict between the current OJS checklist (12 pt, single spacing) and the editorial/reference manuscript style used for the Round-5 Word file (13 pt, 1.2 spacing). Confirm with the journal if necessary before upload.
2. Perform one last Microsoft Word visual check after the final typography decision.
3. Change the submission-data package sharing from editor/writer access to Viewer/read-only before treating it as a frozen research release.
4. Recheck the status of any draft specialised-data standard and update its classification only if an authoritative issued version exists.
