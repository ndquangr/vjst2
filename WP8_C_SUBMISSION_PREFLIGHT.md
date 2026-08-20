# WP8-C submission preflight — VJST 2

**Audit date:** 09/08/2026  
**Submission candidate:** `VJST2_submission_ready.docx`

## 1. Content freeze

The DOCX is converted from the locked WP8-B scientific manuscript. No new scientific claim, architecture decision, legal interpretation or evaluation result was introduced during WP8-C. Conversion changes are limited to Word formatting, explicit numbering/citations, figure insertion, table pagination, accessibility metadata and layout QA.

Locked scientific invariants remain:
- 16-document selected corpus -> 116 source units -> 128 atomic source constraints.
- 128 = 114 class A + 8 class D + 6 class M.
- Class A design-response status = 110 ĐÁP ỨNG + 3 MỘT PHẦN + 1 CẦN LÀM RÕ.
- Initial architecture B1₀ is evaluated with 10 scenarios: 2 direct + 7 conditional + 1 architectural risk (S9).
- S9/S10 are absorbed into the refined design B1-R through AD01/AD03 without re-scoring the original stress-test result.
- No expert walkthrough/review is used as a validation method. Future validation remains objective prototype/repeatable testing.

## 2. Current VJST submission-format checks

Official sources checked on 09/08/2026:
- https://b.vjst.vn/index.php/ban_b/about/submissions
- https://b.vjst.vn/index.php/ban_b/quy-dinh-bai-viet

The current online checklist asks for a Microsoft Word/OpenOffice/RTF submission, 12-point single-spaced text, with figures and tables inline. The reference guidance uses numbered square-bracket citations, English final references in first-appearance order, first three authors + `et al.` when there are more than three authors, and DOI/URL/access date when applicable.

Applied to the submission candidate:
- File type: DOCX.
- Page: A4; margins top/bottom 2 cm, left 3 cm, right 2 cm.
- Main text: Times New Roman specified in DOCX, 12 pt, single spacing.
- Tables: inline, 10 pt where needed for readability; header rows repeat on multi-page core tables; rows are prevented from splitting across pages.
- Figures: 5 inline figures; captions remain with the corresponding figure.
- References: 37 numbered entries, sequence [1]–[37], no missing/unused entries relative to the locked manuscript.
- Vietnamese abstract: 248 words; English abstract: 197 words.
- Author names, affiliations and corresponding email preserved from the editorial reference manuscript; submission dates are not filled in.

`4044_VJST.docx` was used as the editorial reference for front-matter rhythm and presentation. Where its typography differs from the current OJS checklist, the current 12-point/single-spaced checklist is used for this submission candidate.

## 3. Visual and structural QA

Canonical DOCX renderer was run after the final edits and every page was visually inspected.

Final QA render:
- 25 A4 pages in the headless QA environment.
- 5 figures, all visible and readable; Hình 2 was redrawn during conversion to remove overlapping component labels.
- 5 numbered core tables plus the unnumbered R1–R5 and V6 matrices.
- No clipped text, overlapping objects, broken long-table continuation rows or orphan continuation headers observed.
- Core long-table rows do not split across pages.
- 5 figures have descriptive alt text.
- No comments or tracked changes remain in the DOCX.
- PDF render is openable and unencrypted.

Accessibility audit after figure-alt fixes reports no high-severity issue. One medium finding remains because the intentionally unnumbered R1–R5 rule matrix has no separate header row; this does not affect rendering or manuscript content. Raw URLs in references are reported as low-severity accessibility findings but are retained because VJST requests URL information when available.

## 4. Reference and manuscript integrity checks

- 37 reference entries in exact numeric sequence.
- Key citations with page/chapter qualifiers were preserved as human-readable numeric citations in Word.
- No DOI was invented for the previously accepted article; it remains marked accepted for publication / DOI not yet assigned.
- No expert-review/walkthrough validation language is present.
- No Word comments or tracked-change markup is present.
- Current title: **Kiến trúc tham chiếu phân tán tỉnh–trung ương cho nền tảng số quản lý doanh nghiệp khoa học và công nghệ và doanh nghiệp khởi nghiệp sáng tạo**.
- English title: **A provincial–central distributed reference architecture for a digital platform managing science and technology enterprises and innovative startups**.

## 5. Draft specialised-data source

The draft specialised-data standard remains class D in this candidate. Searches of official web sources performed during WP8-C did not locate an authoritative issued version matching the draft reviewed by the study. This is not treated as proof that no later issuance exists; its status must be checked again if the actual upload occurs after 09/08/2026.

## 6. Submission-time recheck only

If the manuscript is uploaded on a later date, recheck only:
1. VJST online submission checklist and reference rules for any change.
2. Whether the draft specialised-data standard has become an authoritative issued document.
3. DOI/status of the already accepted prior article, if assigned by then.
4. Word rendering on the author's local Microsoft Word installation, especially font substitution and figure/table reflow.

No further architecture/content work is required unless one of these submission-time checks changes the evidence base.
