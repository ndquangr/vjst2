# WP7.6 — Legal claim/locator audit

Audit date: 09/08/2026. Scope: claims visible in the manuscript that materially constrain authority, workflow, data sources, interoperability, protection, or transition. The audit checks whether the prose stays at L1 when attributing content to law; architecture consequences remain L2/L3.

| ID | Manuscript claim | Source / locator checked | Result | Action |
|---|---|---|---|---|
| LC01 | Provincial People’s Committee where an S&T enterprise has its headquarters receives, appraises, issues, changes, reissues, revokes and cancels the certificate | NĐ 268/2025/NĐ-CP, khoản 1 Điều 48 | PASS | Intro was tightened to the exact statutory verbs; no broader “lifecycle management” claim is attributed to khoản 1. |
| LC02 | Provincial authority periodically updates certificate data to the national STI management digital platform | NĐ 268, khoản 3 Điều 48 | PASS | Retained as L1. |
| LC03 | Provincial authority/authorized agency notifies the Ministry within 15 days for the decisions listed in the provision | NĐ 268, khoản 2 Điều 66 | PASS | Retained; technical retry/timestamp mechanisms remain L2. |
| LC04 | Completeness check in 03 working days; issue/refuse certificate within 15 days after a valid dossier | NĐ 268, khoản 1–2 Điều 51 | PASS | Used only as business-time constraints, not software latency/SLA. |
| LC05 | Annual S&T-enterprise reporting before 15/12 | NĐ 268, khoản 2 Điều 54 | PASS | Retained as a source-based business deadline. |
| LC06 | Provincial report to the Ministry before 31/3 each year | NĐ 268, khoản 5 Điều 66 | PASS | Retained as a source-based business deadline. |
| LC07 | NĐ 47/2020/NĐ-CP ceased to have effect when NĐ 278 took effect | NĐ 278/2025/NĐ-CP, khoản 2 Điều 23 | PASS | Draft references to NĐ 47 remain diagnostic class D only. |
| LC08 | Mandatory sharing/synchronisation can use the national data sharing/coordination platform; Agent Node is the secured connection component at ministries/localities | NĐ 278, khoản 2–3 Điều 7 | PASS | Supports interoperability boundary, not a product choice. |
| LC09 | National master data follows a single trusted-source principle | NĐ 278, khoản 2 Điều 5 | PASS | Used as L1 rationale for source authority; does not imply one physical database for every domain. |
| LC10 | Organisational e-ID registration verifies organisation information against the national business registration database or other national/sectoral databases | NĐ 69/2024/NĐ-CP, khoản 2 Điều 12 | PASS | Corrected earlier locator remains khoản 2 Điều 12. |
| LC11 | Systems connecting to the electronic identification/authentication system must meet at least information-system security level 3 | NĐ 69, khoản 1 Điều 18 | PASS | Architecture marks this as a pre-deployment condition; no claim that the proposed system already satisfies it. |
| LC12 | Public bodies/public-service providers may request electronic authentication through connected systems/databases; result sharing is constrained | NĐ 69, khoản 1–2,4 Điều 19 | PASS | Retained in V6/interoperability view. |
| LC13 | NĐ 169 modifies selected provisions of NĐ 69 rather than generically replacing it | NĐ 169/2025/NĐ-CP, Điều 43 | PASS | References to NĐ 169 are limited to the specific amendment context. |
| LC14 | NĐ 13/2023/NĐ-CP ceased on 01/01/2026 | NĐ 356/2025/NĐ-CP, khoản 2 Điều 42 | PASS | Corpus classification correctly treats old draft references to NĐ 13 as stale. |
| LC15 | Current personal-data baseline is Law 91/2025/QH15 plus NĐ 356/2025/NĐ-CP | Luật 91/2025/QH15; NĐ 356/2025/NĐ-CP | PASS | Used only for protection/access/audit constraints; no implementation compliance is claimed. |
| LC16 | QĐ 1973 distinguishes master/transaction/source/analysis/open data and identifies organisation/enterprise data source relationships | QĐ 1973/QĐ-BKHCN, Mục III.3.2–III.3.3; related Appendix entries | PASS | Architectural inference is explicitly at attribute-group/source-authority level. |
| LC17 | QĐ 1762 currently lists “CSDL Doanh nghiệp khởi nghiệp” at STT 38 while the draft structures both DN KH&CN and DN KNST domains | QĐ 1762/QĐ-BKHCN, Appendix STT 38; draft Appendix IV/IX | PASS WITH STATUS | Manuscript keeps this as `CẦN LÀM RÕ`, not as a legal conflict. |
| LC18 | Draft MD001/source wording and old legal references are evidence for diagnosis only | Draft `Khung TC DNKHCN final`, Điều 4, Điều 9, Appendix IV/IX | PASS | Class D; never used to create L1 or mandatory architecture. |

## Authoritative verification notes

- Official Government metadata for NĐ 268/2025/NĐ-CP confirms issuance/effect on 14/10/2025 and provides the signed PDF: https://vanban.chinhphu.vn/?classid=1&docid=215663&orggroupid=2&pageid=27160
- VBPL marks NĐ 268/2025/NĐ-CP as in force; the full text was cross-checked for Articles 48, 51 and 66.
- Official Government metadata for NĐ 278/2025/NĐ-CP confirms issuance/effect on 22/10/2025: https://vanban.chinhphu.vn/?docid=215682&pageid=27160
- Official Government metadata was also checked for NĐ 69/2024/NĐ-CP, NĐ 169/2025/NĐ-CP, Law 91/2025/QH15 and NĐ 356/2025/NĐ-CP.

## Audit conclusion

No legal claim was intentionally upgraded from a design inference to a statutory requirement. The most important wording change is the opening claim for Article 48: it now mirrors the statutory authority verbs and leaves the architecture consequences (physical distribution, local execution, versioning, retry, read model) at L2/L3.
