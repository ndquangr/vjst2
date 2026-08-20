# Bài báo kỹ thuật VJST — chuyên mục công nghệ

## Định vị bài

Đây là **bài mới, độc lập**, không phải bản mở rộng của bài chính sách trước đó.

- Bài trước đã được công bố trong **Tạp chí Chính sách và Quản lý Khoa học và Công nghệ (JSTPM), Tập 15 số 2 năm 2026, tr. 45--68**; bản chuẩn để trích dẫn là `JSTPM_paper.pdf`. Bài này trích công trình đó như **một nguồn tài liệu bình thường**, ở phần bối cảnh nghiệp vụ và phần đặt vấn đề; không viết theo kiểu "bổ sung cho bài trước". `4044_VJST.docx` chỉ còn là bản biên tập/chuẩn typography nội bộ và artefact lịch sử cho audit độc lập, **không còn là nguồn trích dẫn**.
- **Phiếu nhận xét của hai phản biện là của bài trước.** Chúng là tài liệu tham khảo nội bộ để tránh lặp lại điểm yếu, **không phải căn cứ cấu trúc** cho bài này. Không mục nào của bài được viết ra để "đáp phản biện".
- Đối tượng bài: chuyên mục **công nghệ**. Trọng tâm là **kiến trúc hệ thống**, không phải phân tích chính sách. Chính sách chỉ xuất hiện ở vai trò **ràng buộc thiết kế**.

## Cấu trúc file

```
main.tex                        điều phối, preamble, gọi các mục
references.tex                  danh mục tài liệu tham khảo VJST
refs.bib                        metadata BibTeX dự phòng
00_frontmatter.tex                tiêu đề, tác giả                  [ĐÃ VIẾT]
01_abstract.tex                   tóm tắt VI + EN, từ khóa          [ĐÃ VIẾT]
02_intro.tex                      giới thiệu                         [ĐÃ VIẾT]
03_background.tex                 cơ sở nghiên cứu/định vị kiến trúc   [FINAL REVIEW — ĐÃ RÚT GỌN]
04_method.tex                     tư liệu và phương pháp             [ĐÃ VIẾT]
05_architecture.tex               kiến trúc hệ thống đề xuất         [ĐÃ VIẾT — lõi]
06_data.tex                       kiến trúc dữ liệu                  [ĐÃ VIẾT — lõi]
07_interop.tex                    liên thông và ranh giới            [ĐÃ VIẾT — lõi]
08_evaluation.tex                 đánh giá kiến trúc theo kịch bản   [WP7.5 ĐÃ MỞ RỘNG S1--S10]
09_discussion.tex                 bàn luận                           [ĐÃ VIẾT]
10_conclusion.tex                 kết luận                           [ĐÃ VIẾT]
```

Mỗi mục nội dung được duy trì độc lập theo file. Ghi chú soạn thảo nằm trong lệnh `\note{}` và được ẩn mặc định ở bản PDF sạch bằng `\renewcommand{\note}[1]{}` trong `main.tex`.

## Biên dịch

```bash
xelatex main.tex && xelatex main.tex && xelatex main.tex
```

Khuyến nghị XeLaTeX cho tiếng Việt. Nếu chỉ có pdfLaTeX, đổi khối font trong `main.tex` theo hướng dẫn ở đầu file.

## Sáu hình và bảy bảng trong thân bài hiện tại (cập nhật sau WP1/WP2)

Sau lượt final review, các bảng/hình mang tính registry, deployment profile hoặc đặc tả chi tiết được chuyển sang `supplementary_material`. Thân bài chỉ giữ các artefact trực tiếp phục vụ lập luận khoa học. WP1 bổ sung Bảng "Hệ thống hiện hữu và ranh giới kế thừa" (đẩy các bảng sau lên một số); WP2 bổ sung Hình máy trạng thái chuyển giao quyền ghi (đẩy Hình Container/P-DIST lên một số).

| Mã | Nội dung | Mục |
|---|---|---|
| Hình 1 | Định vị nền tảng trong hệ quy chiếu kiến trúc số/dữ liệu | Kiến trúc hệ thống |
| Hình 2 | Góc nhìn năng lực--ứng dụng | Kiến trúc hệ thống |
| Hình 3 | Kiến trúc dữ liệu tỉnh--trung ương; topology là điểm biến thiên | Kiến trúc dữ liệu |
| Hình 4 | Máy trạng thái chuyển giao quyền ghi (AD01) -- UML State Machine | Kiến trúc dữ liệu |
| Hình 5 | Cấu trúc Container và ranh giới trách nhiệm theo C4 | Liên thông |
| Hình 6 | Cấu hình triển khai logic P-DIST | Liên thông |
| Bảng 1 | Ranh giới với nghiên cứu trước đã công bố | Giới thiệu |
| Bảng 2 | Hệ thống hiện hữu và ranh giới kế thừa của nền tảng đề xuất | Cơ sở nghiên cứu |
| Bảng 3 | Các quyết định kiến trúc chính và đánh đổi | Kiến trúc hệ thống |
| Bảng 4 | Thẩm quyền dữ liệu ở mức khái quát | Kiến trúc dữ liệu |
| Bảng 5 | Các ranh giới liên thông và hệ quả kiến trúc | Liên thông |
| Bảng 6 | Kết quả stress-test B1 và hậu kiểm B1-R/P-DIST | Đánh giá |
| Bảng 7 | Đối sánh SRA với các khung kiến trúc, dữ liệu và liên thông hiện hành | Bàn luận |

## Ước lượng độ dài

| Mục | Trang |
|---|---|
| Đặt vấn đề | 1,0–1,2 |
| Cơ sở kiến trúc tham chiếu | 1,5–2,0 |
| Phương pháp | 1,0–1,5 |
| Kiến trúc hệ thống | 2,0–2,5 |
| Kiến trúc dữ liệu | 2,0–2,5 |
| Liên thông và ranh giới | 2,0–2,5 |
| Đánh giá kiến trúc | 1,0–1,5 |
| Bàn luận | 1,5–2,0 |
| Kết luận | 0,5–0,8 |
| **Tổng thân bài mục tiêu** | **12,5–16,5** |

Sau WP6, bản QA theo typography gần `4044_VJST.docx` còn **23 trang tổng cộng** (gồm front matter, thân bài và tài liệu tham khảo), giảm từ 46 trang ở WP5. Con số này chỉ phản ánh mức nén hiện tại, **không phải xác nhận giới hạn trang chính thức**. Một bộ hướng dẫn chi tiết trước đây của VJST nêu giới hạn 10 trang, trong khi bản biên tập `4044_VJST.docx` dài 28 trang và checklist nộp bài hiện hiển thị font 12/giãn dòng đơn. Dự án vì vậy tiếp tục dùng `4044_VJST.docx` làm chuẩn trực tiếp về front matter/typography theo chỉ đạo, đồng thời giữ chênh lệch với checklist OJS như một điểm cần xác nhận ở vòng nộp cuối. Chi tiết truy vết 128 mệnh đề ràng buộc nguồn nguyên tử được giữ ở dữ liệu/phụ lục bổ trợ thay vì đưa trở lại thân bài.
Sau các vòng WP7--WP8-B, bản QA hiện là **31 trang** do bổ sung V5/V6, quy tắc tái lập, vòng refinement B1$_0$→B1-R và hai nguồn chuẩn mô hình hóa; đây vẫn là bản QA XeLaTeX, chưa phải DOCX nộp chính thức.
Sau WP9, bản QA XeLaTeX là **41 trang A4** do bổ sung bảng delta với nghiên cứu trước, quy tắc phù hợp CR1--CR9 và hậu kiểm B1-R. Con số này dùng để kiểm tra nội dung/bố cục; môi trường hiện không có Times New Roman nên dùng DejaVu Serif làm font QA, không coi PDF là tệp nộp chính thức.

**Final review/compression 10/08/2026.** Thân bài được biên tập lại theo đúng dạng bài báo khoa học đề xuất kiến trúc, không theo dạng báo cáo kỹ thuật/SRS: Method, Architecture, Data, Interoperability, Background, Introduction, Evaluation và Discussion chỉ giữ câu hỏi/phương pháp, nền tảng học thuật, rationale, bất biến kiến trúc, trade-off, ý nghĩa kết quả và giới hạn; registry, trường dữ liệu, state machine chi tiết, ma trận trust/interoperability, VP/CR, deployment profile, bảng C01--C10 và ma trận kiểm thử kịch bản chi tiết được chuyển sang `supplementary_material`. Sau lượt Discussion, bản QA hiện là **31 trang main + 11 trang supplement**. Thân bài có **4 hình + 5 bảng**; Bảng đánh giá vẫn giữ đủ S1--S10 nhưng chỉ nêu trạng thái trước/sau và hàm ý kiến trúc. Hình Deployment/P-DIST không còn ở thân bài; source của toàn bộ 5 hình vẫn được giữ trong `figure_sources/`.

## Trạng thái kế hoạch chỉnh sửa sau phản biện

- **WP1 — Academic grounding: HOÀN THÀNH 08/08/2026.** Đã bổ sung nền tảng về software reference architecture (Angelov et al.; ISO/IEC/IEEE 42010), software/digital innovation ecosystems (Manikas & Hansen; Wang), reference architecture cho software ecosystems (Knodel & Manikas; Kruize et al.), requirements traceability/regulatory requirements engineering (Winkler & von Pilgrim; Breaux et al.; Kosenkov et al.) và tiền lệ đánh giá reference architecture bằng ATAM (SEI/Gallagher). Các nguồn ngoài project source được kiểm chứng qua trang nhà xuất bản/chuẩn hoặc cổng nghiên cứu chính thức; metadata đã thêm vào `references.tex` và `refs.bib`.
- **WP2 — Atomic traceability: HOÀN THÀNH 08/08/2026.** C01--C10 chỉ là *constraint families* dùng trong thân bài; ma trận bổ trợ đã phân rã thành 128 mệnh đề ràng buộc nguồn nguyên tử Cxx.yy (114 lớp A hiện hành/có thẩm quyền, 8 lớp D dự thảo-chẩn đoán, 6 lớp M tham chiếu/phương pháp). WP2 ban đầu có 100 `ĐÁP ỨNG`, 13 `MỘT PHẦN`, 1 `CẦN LÀM RÕ`; các điểm mở này là đầu vào cho WP3.
- **WP3 — Architecture formalisation/trade-offs: HOÀN THÀNH 08/08/2026.** Đã xác định lớp giải pháp SRA, 6 stakeholder groups, 7 concern groups, 6 viewpoints V1--V6, 8 stable-core principles SC1--SC8, 8 variation points VP1--VP8 và 5 architecture decisions AD01--AD05. Bổ sung AE22/AE23 cho technology realization và security/privacy. Sau formalization: 114/114 A-constraints vẫn có trace link; 110 `ĐÁP ỨNG`, 3 `MỘT PHẦN`, 1 `CẦN LÀM RÕ`. Đây vẫn là **design-response status**, không phải bằng chứng thực nghiệm của hệ thống đã triển khai; WP4 vẫn cần phép thử kiến trúc theo kịch bản.
- **WP4 — Scenario-based architecture evaluation: HOÀN THÀNH 08/08/2026 (được WP7.1 hiệu chỉnh cách diễn giải).** WP4 đã tạo B0/B1 và S1--S8; WP7.1 không còn dùng kết quả để xếp hạng/chọn B1 mà chuyển thành stress-test/trade-off analysis với rubric `ĐÁP ỨNG TRỰC TIẾP / ĐÁP ỨNG CÓ ĐIỀU KIỆN / RỦI RO KIẾN TRÚC`.
- **WP5 — Novelty/delta consistency: HOÀN THÀNH 09/08/2026.** Đã khóa ranh giới với bài trước: FR, kiến trúc sáu lớp, bốn nhóm người dùng và C4 Container trước đây chỉ dùng để xác lập ranh giới novelty/bối cảnh, không tham gia corpus, Cxx.yy, DRV hay tổng hợp SRA. Introduction/Method/Discussion/Conclusion/Abstract hiện thống nhất A1--A4: SRA đa góc nhìn, mô hình phân tán tỉnh--trung ương và quy trình cấu hình; thẩm quyền dữ liệu theo nhóm thuộc tính; liên thông/ranh giới trách nhiệm; truy vết nguyên tử + đánh giá kịch bản.
- **WP6 — Rewrite & compress: HOÀN THÀNH 09/08/2026.** Đã rút bản QA từ 46 xuống 23 trang bằng cách nén prose trùng lặp, gom các giao diện/nhóm dữ liệu/năng lực trong Bảng 1--5 và giữ chi tiết Cxx.yy/AE/AD/VP ở artefact bổ trợ. Các số lõi vẫn giữ nguyên: 128 mệnh đề ràng buộc nguồn nguyên tử (114 A, 8 D, 6 M), trạng thái thiết kế 110 `ĐÁP ỨNG` + 3 `MỘT PHẦN` + 1 `CẦN LÀM RÕ`, AD01--AD05, VP1--VP8, AE24--AE26 và bộ kịch bản B0--B1 (được mở rộng thành S1--S10 ở WP7.5). Tóm tắt tiếp tục nằm trong khoảng mục tiêu của dự án; sau WP8-B có 37/37 tài liệu tham khảo được trích và đúng thứ tự xuất hiện đầu tiên (bổ sung nguồn chính thức cho C4 và ArchiMate 3.2).

- **WP7.1 — Evaluation logic: HOÀN THÀNH 09/08/2026.** B1$_0$ được xác định trước phép thử từ DRV1--DRV5; B0 chỉ là baseline contrast, không phải ablation model. Đã bỏ logic 4--4/"B1 thắng", thêm rubric ba mức, đổi Bảng 5 thành stress-test B1$_0$ và nêu rõ so sánh không có giá trị suy luận nhân quả cho một quyết định riêng lẻ.
- **WP7.2 — Distributed province--central terminology/topology: HOÀN THÀNH 09/08/2026.** Thuật ngữ chính đổi từ "liên bang/CSDL liên bang" sang **kiến trúc phân tán tỉnh--trung ương** và **nút dữ liệu nghiệp vụ cấp tỉnh (AE24)**. Hiện thực hóa mục tiêu vẫn giữ một kho dữ liệu vận hành vật lý tách biệt cho mỗi tỉnh, nhưng không đồng nhất với một CSDL chuyên ngành độc lập về pháp lý. AD01 được viết lại: L1 xác lập jurisdiction boundary; topology vật lý là L2 dựa thêm trên DRV2--DRV3 và phải giữ DRV4--DRV5.
- **WP7.3 — Deployment + security/privacy views and notation: HOÀN THÀNH 09/08/2026.** V5 đã có Hình 5 theo C4 Deployment, tách deployment node/container instance/infrastructure node; V6 đã có ma trận Z1--Z5 về biên tin cậy, quyền, kiểm soát và audit owner. Hình 4 được giữ đúng mức C4 Container, Hình 2 bỏ kiểu phần tử trộn `Business Role / Interface`, Hình 3 chỉ dùng Access giữa Application Component--Data Object và Flow giữa Application Components. C08.05 vẫn `MỘT PHẦN` vì cấp độ ATTT phải có bằng chứng triển khai.
- **WP7.4 — Atomic-traceability reproducibility: HOÀN THÀNH 09/08/2026.** Đã formalize R1--R5, phân biệt 128 `atomic source constraints` với các yêu cầu ngữ nghĩa đã khử trùng lặp, và lập chỉ mục **116 đơn vị nguồn**; 4 đơn vị nguồn được tách thành nhiều Cxx.yy theo R2. `constraint_traceability.csv` có thêm `source_unit_id`, `atomization_rule`, `sibling_constraint_ids`; bổ sung `source_unit_index.csv`, `atomization_rules.csv`, `worked_traceability_examples.csv` và phụ lục E1--E3. Method có worked example điểm c khoản 2 Điều 43 và khoản 2 Điều 66 NĐ 268, cùng ví dụ R3 về C05.09/C06.12.
  Bản QA sau WP7.4 là **27 trang**; việc tăng trang đến từ V5/V6 (WP7.3) và giao thức R1--R5/worked examples, không phải đưa ma trận 128 dòng trở lại thân bài.
- **WP7.5 — Scenario stress-test extension: HOÀN THÀNH 09/08/2026.** Đã mở rộng S1--S8 thành **S1--S10**. S9 kiểm tra chuyển phạm vi quản lý/quyền ghi giữa hai tỉnh theo thời gian và được phân loại `RỦI RO KIẾN TRÚC`; S10 kiểm tra nâng cấp lược đồ/quy trình không đồng thời và được phân loại `ĐÁP ỨNG CÓ ĐIỀU KIỆN`. Kết quả mới: **2 trực tiếp + 7 có điều kiện + 1 rủi ro**. WP8-A đã hấp thụ R-S9 vào AD01 của B1-R dưới dạng gán quyền ghi theo khoảng hiệu lực/single-active-writer và hấp thụ R-S10 vào AD03 dưới dạng compatibility window/minimum supported version/version pinning. Đây là quyết định L2 đã thuộc artefact cuối, nhưng vẫn phải được kiểm tra bằng prototype, rolling-upgrade và historical-replay tests. Bản QA sau WP7.5 là **28 trang**; tóm tắt tiếng Việt được giữ ở khoảng 250 từ.

- **WP7.6 — Legal/reference/claim audit: HOÀN THÀNH 09/08/2026.** Hướng kiểm chứng tiếp theo chỉ dùng bằng chứng khách quan từ nguyên mẫu và các phép thử có thể lặp lại. Claim mở đầu về khoản 1,3 Điều 48 NĐ 268 được viết sát nội dung nguồn; các claim pháp lý trọng yếu được audit lại theo locator. Danh mục tham khảo được chỉnh theo quy định VJST hiện hành: hơn 3 tác giả ghi 3 tác giả đầu + `et al.`, bổ sung URL/ngày truy cập cho các nguồn trực tuyến/chính thức đã kiểm chứng.

- **WP8-A — DSR refinement + independence from prior paper: HOÀN THÀNH 09/08/2026.** Phân biệt B1$_0$ trước stress-test và B1-R sau tinh chỉnh. R-S9 được hấp thụ vào AD01 bằng gán quyền ghi theo thời gian với bất biến single-active-writer; R-S10 được hấp thụ vào AD03 bằng cửa sổ tương thích, phiên bản tối thiểu và ghim phiên bản. Bài trước chỉ còn vai trò xác lập ranh giới đóng góp/bối cảnh; pipeline hiện tại độc lập: nguồn hiện hành → đơn vị nguồn → Cxx.yy → DRV1--DRV5 → AD/AE → B1$_0$ → stress-test → B1-R.
- **WP8-B — Notation + corpus/scenario reproducibility + consistency hardening: HOÀN THÀNH 09/08/2026.** Đã khóa D1--D4 cho lựa chọn tài liệu và `corpus_manifest.csv` gồm 16 tài liệu (13 A, 1 D, 2 M); bổ sung COV1--COV5 và `scenario_coverage.csv` để truy nguyên cách sinh/bao phủ S1--S10. Registry stakeholder chuyển sang STK1--STK6 để không trùng mã kịch bản. Hình 1--3 được rà lại theo ArchiMate 3.2; Hình 4 dùng các abstraction C4 Container ở mức logic và ghi rõ công nghệ/giao thức chưa khóa ở L3; Hình 5 tách Deployment Node/Container instance/Infrastructure Node. Hình 3--5 đã được vẽ lại để loại giao cắt/chồng nhãn. Bản QA sau WP8-B là **31 trang**, 37/37 tài liệu tham khảo dùng đúng thứ tự xuất hiện; các số lõi 116/128, 114/8/6, 110/3/1 và 2/7/1 không đổi.

- **WP9.1 — Core/profile separation: HOÀN THÀNH 09/08/2026.** Lõi SRA chỉ khóa biên quyền ghi theo thẩm quyền, provenance và quản trị phiên bản; topology có thể là kho tập trung đa tenant, phân vùng logic/schema, kho vật lý theo tỉnh hoặc mô hình lai. P-DIST là profile triển khai dẫn xuất để stress-test, không phải nghĩa vụ pháp lý hay cấu hình mặc định tối ưu.
- **WP9.2 — Conformance rules: HOÀN THÀNH 09/08/2026.** Bổ sung CR1--CR9 cho lõi-phù-hợp và PD1--PD2 cho P-DIST-phù-hợp trong `conformance_rules.csv`; thân bài công bố điều kiện phù hợp và cách cấu hình dẫn xuất B1-R/P-DIST.
- **WP9.3 — S9 protocol and post-refinement check: HOÀN THÀNH 09/08/2026.** AD01/CR2--CR3 xác định `write_scope`, `writer_epoch`, fencing và máy trạng thái chuyển quyền ghi; S1--S10 được chấm lại trên B1-R/P-DIST. Kết quả hậu kiểm: **2 trực tiếp + 8 có điều kiện + 0 rủi ro kiến trúc chưa hấp thụ ở L2**; bằng chứng triển khai vẫn để mở.
- **WP9.4 — Reproducibility numbers and release placeholders: HOÀN THÀNH 09/08/2026.** Chuỗi số được khóa ở 16 tài liệu → 116 đơn vị nguồn → 128 dòng truy vết (114 A, 8 D, 6 M), với trạng thái A là 110/3/1. Mục dữ liệu bổ trợ có placeholder URL/tag/commit/checksum phải thay bằng bản phát hành chỉ đọc trước khi nộp.
- **WP9.5 — Independence audit against prior work: HOÀN THÀNH 09/08/2026.** Bổ sung `prior_work_delta.csv` và Bảng 1; nghiên cứu trước chỉ xác lập ranh giới đóng góp. Đối chiếu n-gram ban đầu dùng bản biên tập `4044_VJST.docx` và không phát hiện trùng lặp nội dung thực chất; các chuỗi trùng dài chỉ thuộc tên tác giả/cơ quan/địa chỉ. Từ 10/08/2026, nguồn trích dẫn chuẩn của nghiên cứu trước được thay bằng bản công bố `JSTPM_paper.pdf`.
- **WP9.6 — Compression, build and visual QA: HOÀN THÀNH 10/08/2026.** Gộp bảng kết quả B1$_0$/B1-R, loại diễn giải bảo vệ novelty bị lặp, sửa tràn lề và bọc chú giải sơ đồ. Cập nhật trích dẫn nghiên cứu trước từ accepted manuscript sang bản công bố `JSTPM_paper.pdf` (JSTPM, Tập 15 số 2, 2026, tr. 45--68), đổi locator trong thân bài sang trang công bố thực (tr. 54, 58--59) và loại mã nội bộ `4044` khỏi prose/bảng của bản thảo. XeLaTeX được build lại và visual QA lại sau cập nhật; kết quả build cuối được ghi trong `WP9_IMPLEMENTATION_AUDIT.md`.
- **Round-3 strengthening — HOÀN TẤT 10/08/2026.** Sau vòng phản biện bổ sung, bản Word submission được gia cố theo ba hướng nhưng không quay lại dạng SRS: (i) khái quát ba design principles có điều kiện từ hai đóng góp kiến trúc; (ii) thêm Bảng 6 đối sánh SRA với QĐ 3090, QĐ 292, QĐ 2439/NĐ 278, QĐ 1973, NĐ 268 và các ràng buộc định danh/bảo vệ dữ liệu; (iii) đưa Hình 5 C4 Deployment logic của P-DIST vào thân bài, với nhãn rõ đây là profile L2 dùng stress-test, không phải topology bắt buộc. Bản Word `VJST2_submission_round3_strengthened.docx` theo format 4044/JSTPM có **30 trang, 5 hình, 6 bảng**, đã render và visual-QA toàn bộ; không có tracked changes/comments. Các source TeX liên quan cũng được đồng bộ nội dung Round-3, nhưng Word là artefact submission chính.



### Artefact bổ trợ WP2--WP3

- `constraint_traceability.csv`: ma trận 128 mệnh đề ràng buộc nguồn nguyên tử có thể kiểm tra/máy đọc; sau WP7.4 có thêm mã đơn vị nguồn và quan hệ sibling để tái lập phép tách.
- `source_unit_index.csv`: chỉ mục 116 cặp nguồn--locator và danh sách Cxx.yy sinh ra từ từng đơn vị nguồn.
- `corpus_manifest.csv` / `corpus_selection_rules.csv`: danh mục 16 tài liệu và quy tắc D1--D4 cho lựa chọn tập nguồn ở cấp tài liệu.
- `scenario_coverage.csv` / `scenario_coverage_rules.csv`: ma trận COV1--COV5, liên kết S1--S10 với DRV1--DRV5 và V1--V6.
- `stakeholder_registry.csv`: sổ STK1--STK6, tách namespace stakeholder khỏi S1--S10.
- `notation_registry.csv`: hồ sơ ký pháp/phạm vi biểu diễn của Hình 1--5.
- `WP8_B_reproducibility_notation_supplement.pdf`: phụ lục QA 3 trang về lựa chọn nguồn, bao phủ kịch bản và ký pháp.
- `WP8_B_AUDIT.md`: audit Lượt B về notation, reproducibility, consistency, build/preflight và citation order.
- `atomization_rules.csv`: giao thức R1--R5 ở dạng máy đọc được.
- `worked_traceability_examples.csv`: ba worked examples E1--E3 cho R2, truy vết L1--L2--L3 và R3/provenance.
- `WP7_4_traceability_reproducibility_supplement.pdf`: phụ lục tái lập phép mã hóa nguyên tử.
- `constraint_traceability.tex`: bản trình bày ma trận đầy đủ; **không** chèn vào thân bài để tránh biến bài báo thành đặc tả dài.
- `constraint_traceability_supplement.pdf`: phụ lục độc lập để kiểm tra trực quan ma trận 128 dòng.
- `architecture_elements.csv`: sổ đăng ký AE01--AE26.
- `viewpoint_registry.csv`: sổ sáu viewpoint V1--V6; sau WP7.3 mọi viewpoint đều có artefact trong thân bài.
- `deployment_view.csv`: hồ sơ máy đọc được cho V5/C4 Deployment.
- `security_privacy_view.csv`: hồ sơ máy đọc được cho V6 trust-zone/control matrix.
- `architecture_decisions.csv`: sổ AD01--AD05 với phương án thay thế, lý do, đánh đổi và liên kết truy vết.
- `architecture_drivers.csv`: sổ DRV1--DRV5 dùng để hình thành B1$_0$ trước phép thử kịch bản.
- `evaluation_rubric.csv`: rubric ba mức của WP7.1 cho đánh giá B1$_0$.
- `variation_points.csv`: sổ VP1--VP8 và phần lõi không được phá vỡ.
- `evaluation_scenarios.csv` / `evaluation_results.csv`: bộ **10 kịch bản S1--S10** stress-test B1$_0$ và đối chiếu B0 theo rubric WP7.1; sau WP7.5 kết quả là 2 trực tiếp, 7 có điều kiện, 1 rủi ro kiến trúc.
- `evaluation_results_b1r.csv`: phép chấm lại S1--S10 trên B1-R/P-DIST bằng cùng rubric; kết quả 2 trực tiếp, 8 có điều kiện, không còn rủi ro kiến trúc chưa hấp thụ ở L2.
- `conformance_rules.csv`: CR1--CR9 của lõi SRA và PD1--PD2 dành riêng cho profile P-DIST.
- `prior_work_delta.csv`: ma trận câu hỏi--đầu vào--phương pháp--sản phẩm--đánh giá--hình/sơ đồ để khóa ranh giới với nghiên cứu trước.
- `evaluation_refinements.csv`: R-S9/R-S10 đã tích hợp vào B1-R ở mức thiết kế L2; trạng thái kiểm chứng triển khai vẫn để mở.
- `architecture_refinement_log.csv`: nhật ký DSR từ B1$_0$ qua S9/S10 và R-S9/R-S10 tới B1-R.
- `WP8_A_refinement_independence_supplement.pdf`: phụ lục tóm tắt vòng tinh chỉnh và ranh giới độc lập với nghiên cứu trước.
- `WP7_5_scenario_stress_test_supplement.pdf`: phụ lục trực quan S1--S10; R-S9/R-S10 được ghi rõ là đã hấp thụ vào B1-R ở mức L2.
- `LEGAL_CLAIM_AUDIT.md`: audit các claim pháp lý trọng yếu và locator.
- `VJST_FORMAT_AUDIT.md`: audit yêu cầu định dạng/hand-off VJST hiện hành dùng cho vòng nộp cuối.
- `supplementary_material.tex` / `supplementary_material.pdf`: gói phụ lục hợp nhất cho chi tiết tái lập, ma trận liên thông, P-DIST/V6, VP1--VP8, CR1--CR9/PD1--PD2 và ánh xạ năng lực đã rút khỏi thân bài.
- `figure_sources/`: source TikZ/LaTeX độc lập của Hình 1--5, PDF preview và `build_figures.sh` để chỉnh và build hình riêng.

- Lớp nguồn `A` = authoritative/current và tạo baseline; `D` = draft/diagnostic, không tính mẫu số; `M` = method/reference, không phải nghĩa vụ pháp lý Việt Nam.
- Trạng thái của lớp A: `ĐÁP ỨNG`, `MỘT PHẦN`, `CHƯA ĐÁP ỨNG`, `CẦN LÀM RÕ`, `XUNG ĐỘT`; D dùng `KHÔNG CHẤM`, M dùng `THAM CHIẾU`.

## Việc còn treo

- Bài dùng đánh giá kiến trúc trước triển khai bằng truy vết và stress scenarios. **S9 là rủi ro của B1_0 và đã buộc tinh chỉnh AD01; S10 buộc mở rộng AD03 để tạo B1-R.** Việc tích hợp refinement là quyết định thiết kế L2, không phải bằng chứng triển khai; nguyên mẫu vẫn phải kiểm thử các bất biến và điều kiện tương thích. Không tạo số liệu giả để điền ngưỡng phi chức năng.
- Sau WP8-B, Hình 1--3 đã được hardening theo profile ArchiMate 3.2 và Hình 4--5 theo các abstraction C4 tương ứng; Hình 3--5 đã được vẽ lại để loại chồng nhãn/giao cắt chữ. Chỉ vẽ lại ở vòng DOCX nếu reflow yêu cầu, không thay đổi model semantics đã khóa.
- Trạng thái ban hành của dự thảo khung tiêu chuẩn dữ liệu chuyên ngành — hiện trích dẫn như dự thảo.
- Trước bản DOCX nộp chính thức, rà lại DOI/URL của tài liệu tham khảo và bổ sung URL chính thức ở những nguồn có thể xác minh; không tự tạo URL/DOI cho văn bản chưa kiểm chứng.

## Quy tắc bắt buộc về thuật ngữ và trích dẫn

Các quy tắc dưới đây áp dụng cho **toàn bộ bài** và được kiểm tra ở mỗi lượt biên tập.

1. **Từ viết tắt và thuật ngữ tiếng Anh ở lần xuất hiện đầu tiên.** Trong phần tiếng Việt, lần đầu phải viết theo mẫu: *thuật ngữ tiếng Việt* (*English term*, **ABBR**), ví dụ: “nghiên cứu khoa học thiết kế (*Design Science Research*, DSR)” hoặc “giao diện lập trình ứng dụng (*Application Programming Interface*, API)”. Các lần sau mới dùng từ viết tắt. Nếu văn bản nguồn chỉ công bố ký hiệu nhưng **không cho dạng tiếng Anh đầy đủ**, không tự suy đoán; viết tên/giải thích tiếng Việt và ghi “theo ký hiệu của [nguồn]”. Trong Abstract tiếng Anh, từ viết tắt cũng phải được mở rộng ở lần đầu xuất hiện.
2. **Không dùng khái niệm tiếng Anh không chú giải.** Với các khái niệm kỹ thuật như *design artefact*, *authoritative source*, *workflow*, *benchmark*, *availability*, *throughput*, v.v., lần đầu phải có diễn giải tiếng Việt tương ứng. Ưu tiên dùng thuật ngữ tiếng Việt trong mạch văn; chỉ giữ tiếng Anh trong ngoặc khi cần đối chiếu thuật ngữ chuyên môn.
3. **Văn bản quy phạm pháp luật phải có định vị điều khoản.** Mọi mệnh đề rút ra từ luật/nghị định phải ghi tối thiểu **Điều + Khoản**, và ghi **Điểm** nếu mệnh đề nằm ở một điểm cụ thể, ví dụ: “điểm b khoản 2 Điều 11”. Không ghi chung “theo Điều 11--13” nếu câu đang dựa vào một khoản cụ thể. Khi một câu tổng hợp nhiều nghĩa vụ, liệt kê từng điều/khoản tương ứng.
4. **Quyết định, khung kiến trúc và phụ lục phải có vị trí nguồn.** Khi trích quyết định/khung, ghi Chương/Mục/Tiểu mục/Phụ lục/STT hoặc tên bảng/hình tương ứng nếu văn bản có cấu trúc đó. Không chỉ dẫn chung toàn văn bản nếu có thể định vị chính xác hơn.
5. **Báo cáo, sách, white paper và tài liệu hướng dẫn phải có số trang thực.** Mọi nhận định nội dung lấy từ các nguồn này phải dùng trích dẫn kèm trang, ví dụ `\citep[pp.~22--30]{eif2017}`. Nếu dựa vào hình/bảng, ghi cả số hình/bảng và trang khi có. Không dùng số trang ước đoán từ mục lục; phải kiểm tra trang thực của PDF/bản gốc.
6. **Số liệu phải truy nguyên được.** Mọi số liệu ngoài văn bản pháp luật phải ghi nguồn, năm/kỳ quan sát, đơn vị/mẫu số khi cần, và **trang/bảng/hình** chứa số liệu. Không đưa số liệu chỉ có trong nguồn thứ cấp nếu nguồn gốc ban đầu không kiểm chứng được.
7. **Không đoán vị trí trích dẫn.** Nếu chưa xác minh được Điều/Khoản hoặc số trang, tạm đánh dấu bằng `\note{CẦN XÁC MINH NGUỒN}` và chưa dùng mệnh đề đó để kết luận. Không điền số trang hoặc điều khoản theo trí nhớ.
8. **Phân biệt căn cứ và suy luận thiết kế.** Trích dẫn nguồn chỉ chứng minh mệnh đề mà nguồn thực sự nêu. Hệ quả kiến trúc do tác giả suy ra phải được đánh dấu L2; lựa chọn kỹ thuật chưa được nguồn bắt buộc phải là L3. Không gắn ngược lựa chọn L2/L3 cho văn bản pháp luật như thể văn bản đã quy định chi tiết kỹ thuật.
9. **Tài liệu tham khảo phải đủ siêu dữ liệu.** Với bài báo: tác giả, năm, tên bài, tạp chí, tập/số, trang, DOI nếu có. Với báo cáo/sách: tác giả/tổ chức, năm, tên, nhà xuất bản/cơ quan, DOI/ISBN nếu có. Với văn bản pháp luật: số hiệu, ngày ban hành, cơ quan ban hành. Không tự tạo DOI hoặc thông tin thư mục chưa kiểm chứng.
10. **Rà soát trước mỗi bản nộp.** Tìm toàn bài các mẫu từ viết tắt/thuật ngữ tiếng Anh chưa mở rộng; các trích dẫn nghị định thiếu Khoản/Điểm; các `\citep{...}` tới báo cáo/sách không có post-note trang; và mọi con số không có locator nguồn.

11. **Hình kiến trúc phải dùng ngôn ngữ mô hình hóa chuẩn.** Mọi hình mô tả kiến trúc phần mềm, kiến trúc hệ thống, kiến trúc dữ liệu, thành phần hoặc tương tác phải chọn và tuân thủ một ngôn ngữ/ký pháp mô hình hóa phù hợp với mục đích của hình, ưu tiên: **C4 Model** cho ranh giới hệ thống và các mức Context/Container/Component; **ArchiMate** cho quan hệ giữa các lớp nghiệp vụ--ứng dụng--dữ liệu--công nghệ ở mức kiến trúc doanh nghiệp; **UML** (Component, Deployment, Sequence, State Machine, Class/Package) cho cấu trúc và hành vi chi tiết. Caption hoặc chú giải của hình phải ghi rõ loại biểu đồ/góc nhìn và ký pháp sử dụng. Không dùng sơ đồ hộp--mũi tên tự chế như một hình kiến trúc trong bản nộp. TikZ, PlantUML, Mermaid, diagrams.net hoặc công cụ tương tự chỉ là **công cụ vẽ**; ngữ nghĩa của phần tử và quan hệ vẫn phải theo ngôn ngữ mô hình hóa đã chọn. Không trộn tùy ý ngữ nghĩa C4, ArchiMate và UML trong cùng một hình; nếu cần nhiều góc nhìn thì tách hình hoặc nêu rõ profile/legend. Hình tạm chưa đạt ký pháp phải gắn `\note{CẦN VẼ LẠI THEO ...}` và không được coi là hình cuối để nộp.


11a. **Kiến trúc tham chiếu phải có phạm vi và rationale kiểm chứng được.** Khi bài dùng thuật ngữ SRA, phải chỉ ra lớp giải pháp, stakeholders/concerns, viewpoints, phần lõi ổn định và variation points; các quyết định kiến trúc quan trọng phải có mã AD, phương án thay thế, lý do, đánh đổi và trace về Cxx.yy/AEyy. Không coi một sơ đồ phân lớp hoặc một cấu hình triển khai cụ thể là toàn bộ SRA. Việc formalize AD/VP không thay thế kiểm chứng triển khai; WP4/WP7 dùng đánh giá theo kịch bản lấy cảm hứng từ ATAM để thử thách các quyết định, còn xác nhận tiếp theo phải dựa trên nguyên mẫu và các phép thử có thể lặp lại đối với liên thông, chuyển quyền ghi, nâng cấp, phục hồi, an toàn và thuộc tính chất lượng.

11b. **Atomic traceability phải tái lập được.** C01--C10 chỉ là constraint families; Cxx.yy là `atomic source constraint`, không mặc nhiên là yêu cầu ngữ nghĩa duy nhất. Phải áp dụng R1--R5, bảo toàn source/locator và không gộp các nguồn tương đồng làm mất provenance. Mỗi Cxx.yy phải truy được tới `source_unit_id`; khi một source unit sinh nhiều Cxx.yy phải có sibling list. L1 chỉ sinh từ nguồn A minh thị; L2/L3 nằm ở đáp ứng/rationale, không được đếm thêm vào số source constraints.


## Quy tắc định dạng VJST-MOST (rà soát 10/08/2026)

12. **Front matter theo bản biên tập 4044_VJST.docx.** Tiêu đề Việt/Anh in đậm; tác giả giữ đúng thứ tự Nguyễn Đình Quảng¹, Nguyễn Huy Cường²*; cơ quan và địa chỉ trình bày Việt/Anh; tác giả liên hệ: nguyenhuycuong@mst.gov.vn. Không tự điền ngày nhận/chuyển phản biện/chấp nhận đăng cho bài mới.
13. **Tóm tắt mục tiêu 160--250 từ cho mỗi ngôn ngữ.** Phạm vi này được giữ theo bộ hướng dẫn chi tiết VJST đã dùng trong dự án và tương thích với cách trình bày của bản biên tập 4044; trang `Quy định bài viết` hiện hành chủ yếu quy định trích dẫn/tài liệu tham khảo. Tóm tắt phải có mục đích, phương pháp, kết quả và kết luận chính; không đưa trích dẫn. Từ khóa Việt/Anh sắp xếp theo thứ tự alphabet và có ít nhất 3 từ khóa. Bản hiện tại dùng chỉ số phân loại 1.2 (Khoa học máy tính và thông tin) và 2.2 (Kỹ thuật điện, điện tử, thông tin), phù hợp định vị bài kiến trúc hệ thống; rà soát lại khi chọn chuyên mục trên hệ thống nộp.
14. **Kiểu chữ và trang.** Dùng Times New Roman 13 pt và giãn dòng 1,2 theo 4044_VJST.docx; nội dung bảng 10 pt, caption 13 pt; khoảng cách đoạn 3 pt và thụt dòng đầu 1,27 cm; khổ A4, lề trên/dưới 2 cm, trái 3 cm, phải 2 cm theo quy định chi tiết của VJST. Nếu môi trường biên dịch không có Times New Roman, chỉ dùng font thay thế để QA nội bộ, không coi là bản nộp.
15. **Tài liệu tham khảo cuối bài phải bằng tiếng Anh và theo thứ tự xuất hiện.** Nguồn không phải tiếng Anh dịch tiêu đề sang tiếng Anh và ghi `(in Vietnamese)`; bài báo <=3 tác giả liệt kê đủ, >3 tác giả liệt kê 3 tên đầu + `et al.`; DOI/URL/ngày truy cập bổ sung khi có. `references.tex` là danh mục dùng để biên dịch bản nộp; `refs.bib` chỉ giữ metadata dự phòng.
16. **Không suy diễn từ sự không thống nhất của hướng dẫn.** Trang `Gửi bài trực tuyến` hiện ghi font 12, giãn dòng đơn, trong khi bộ hướng dẫn chi tiết trước đây ghi font 13 và tối đa 10 trang; bản 4044_VJST.docx dùng 13 pt, giãn dòng 1,2. Khi có xung đột, ưu tiên mẫu biên tập 4044 cho typography và front matter, nhưng ghi nhận giới hạn 10 trang là rủi ro cần xác nhận với tòa soạn trước nộp cuối.

17. **Định dạng tệp nộp.** Checklist `Gửi bài trực tuyến` hiện yêu cầu OpenOffice, Microsoft Word hoặc RTF và yêu cầu hình/bảng nằm đúng vị trí trong thân bài. Dự án vẫn duy trì nguồn chuẩn bằng TEX theo yêu cầu làm việc; khi nộp chính thức cần xuất/chuyển sang DOCX và kiểm tra trực quan theo mẫu biên tập 4044_VJST.docx, không gửi PDF/TEX như tệp bản thảo chính nếu hệ thống không cho phép.
