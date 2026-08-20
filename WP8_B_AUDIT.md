# WP8-B AUDIT — notation, reproducibility, consistency hardening

Ngày khóa: 09/08/2026

## 1. Phạm vi lượt B

Lượt B thực hiện ba gói đã thống nhất:

- **WP8.3 — hardening ký pháp và hình kiến trúc**: khóa profile H1--H5, tách rõ ArchiMate/C4, ghi rõ phần công nghệ/giao thức chưa khóa ở L3 và vẽ lại các hình có giao cắt/chồng nhãn.
- **WP8.4 — tái lập lựa chọn tập nguồn và bộ kịch bản**: bổ sung quy tắc D1--D4 ở cấp tài liệu, manifest 16 tài liệu, quy tắc COV1--COV5 và ma trận S1--S10 × DRV × viewpoint.
- **WP8.5 — consistency/claim/term audit**: kiểm tra namespace, thuật ngữ, số liệu lõi, thứ tự tài liệu tham khảo, build/preflight và render.

Không thay đổi thesis khoa học đã khóa ở WP8-A: B1$_0$ được stress-test, S9/S10 tạo refinement, và artefact cuối là B1-R.

## 2. WP8.3 — ký pháp và hình kiến trúc

### 2.1. Profile H1--H5

`notation_registry.csv` hiện khóa:

- H1: ArchiMate 3.2 — Constraint, Application Component, Association, Flow.
- H2: ArchiMate 3.2 — Capability, Application Component, Association, Flow; Association chỉ là ánh xạ hỗ trợ vì lớp behavior/service trung gian được lược bỏ.
- H3: ArchiMate 3.2 — Application Component, Data Object, Access, Flow.
- H4: C4 logical Container view — Person, Container, Software System, quan hệ một chiều có nhãn; technology/protocol chưa khóa ở L3.
- H5: C4 Deployment — Deployment Node, Container instance, Infrastructure Node; môi trường/công nghệ cụ thể ở L3.

`viewpoint_registry.csv` dùng STK1--STK6 thay vì S1--S6 cho stakeholder, tránh xung đột namespace với kịch bản S1--S10.

### 2.2. Thay đổi hình

- **H1--H2**: giữ layout vì render sạch; làm rõ semantics trong prose và legend.
- **H3**: vẽ lại. Loại nhãn Access lặp, dùng legend cho kiểu đường, tăng khoảng cách dọc và định tuyến các quan hệ Access dùng chung ra ngoài hộp Data Object. Render trang 16 không còn đường đi xuyên chữ/hộp.
- **H4**: vẽ lại thành cấu trúc logic gọn: 3 Person, 6 Container/Database container, 4 Software System ngoài biên. Loại cặp mũi tên đối nghịch dày đặc; các hệ thống ngoài đi qua cổng tích hợp; quan hệ một chiều có nhãn. Technology/protocol được ghi là chưa khóa ở L3 thay vì suy đoán.
- **H5**: vẽ lại. Hai Deployment Node tách rõ, container instances xếp theo cột, Infrastructure Node nằm ngoài; quan hệ nội bộ đi qua side corridors để không cắt nhãn/nút.

TikZ chỉ còn vai trò công cụ vẽ; semantics được khóa bởi profile trong `notation_registry.csv` và prose/caption tương ứng.

## 3. WP8.4 — tái lập tập nguồn

### 3.1. Hai tầng tái lập

Bài hiện phân biệt rõ:

1. **lựa chọn tài liệu**: document universe → selected corpus theo D1--D4;
2. **mã hóa ràng buộc**: selected corpus → 116 source units → 128 atomic source constraints theo R1--R5.

`corpus_manifest.csv` có **16 tài liệu**:

- 13 lớp A;
- 1 lớp D;
- 2 lớp M.

`corpus_selection_rules.csv` lưu D1--D4 ở dạng máy đọc được. Method ghi rõ đây là phạm vi có thể kiểm tra lại tại ngày cắt, **không tuyên bố bao phủ mọi tài liệu có thể liên quan ngoài tiêu chí đã nêu**.

## 4. WP8.4 — tái lập bộ kịch bản

Bộ S1--S10 được tổ chức theo năm chiều bao phủ:

- COV1: vận hành bình thường/biến thể địa phương — S1,S2;
- COV2: thay đổi quy định/nguồn/phiên bản — S3,S6,S10;
- COV3: gián đoạn hạ tầng/lớp trung ương — S4,S7;
- COV4: tổng hợp toàn quốc/quan hệ xuyên địa bàn — S5,S8;
- COV5: chuyển quyền quản lý/ghi — S9.

`scenario_coverage.csv` xác nhận:

- DRV1 = 3 scenario; DRV2 = 3; DRV3 = 2; DRV4 = 7; DRV5 = 7;
- V1 = 5; V2 = 3; V3 = 6; V4 = 10; V5 = 6; V6 = 6.

Mỗi DRV xuất hiện ít nhất hai lần và mọi viewpoint V1--V6 được ít nhất một scenario thử. Method/Discussion đồng thời ghi limitation: ma trận này làm rõ **phạm vi đã thử**, không chứng minh S1--S10 là tập đầy đủ mọi tình huống.

## 5. WP8.5 — consistency audit

### 5.1. Các số lõi

Đối soát trực tiếp từ CSV:

- 116 source units;
- 128 atomic source constraints = 114 A + 8 D + 6 M;
- lớp A = 110 `ĐÁP ỨNG` + 3 `MỘT PHẦN` + 1 `CẦN LÀM RÕ`;
- 10 scenarios;
- B1$_0$ = 2 `ĐÁP ỨNG TRỰC TIẾP` + 7 `ĐÁP ỨNG CÓ ĐIỀU KIỆN` + 1 `RỦI RO KIẾN TRÚC`;
- Hình 1--5 đều có label/caption và được tham chiếu trong registry/prose.

Không thay đổi các số trên trong WP8-B.

### 5.2. Tài liệu tham khảo

Audit script trên toàn bộ `00_frontmatter.tex`--`10_conclusion.tex` và `references.tex`:

- 37 citation keys được dùng;
- 37 `bibitem`;
- 0 thiếu;
- 0 thừa;
- thứ tự `bibitem` khớp **chính xác** thứ tự xuất hiện đầu tiên.

Hai nguồn bổ sung là trang chính thức C4 model và ArchiMate 3.2, dùng để khóa semantics/profile cho H1--H5.

### 5.3. Thuật ngữ và claim

- C10 được diễn đạt là **nghiên cứu sử dụng bốn lớp EIF để kiểm tra liên thông**, không biến nguồn lớp M thành nghĩa vụ pháp lý.
- API được mở rộng lần đầu thành “giao diện lập trình ứng dụng (Application Programming Interface, API)”.
- Agent Node chỉ ghi “theo ký hiệu của NĐ 278”, không tự tạo dạng tiếng Anh đầy đủ.
- Các từ tiếng Anh còn xuất hiện trong hình như Constraint, Application Component, Capability, Data Object, Access, Flow, Person, Container, Deployment Node... là **tên loại phần tử/quan hệ của ký pháp**, đã được giải thích ở prose/legend.
- English title khóa thành “A provincial--central distributed reference architecture ...”; English abstract dùng cùng cách gọi `provincial--central`.
- Không phát hiện claim mới về hiệu năng, SLA kỹ thuật, compliance vận hành hay bằng chứng triển khai.

## 6. Build, preflight và render

### Main manuscript

- XeLaTeX: 3 lượt thành công.
- QA PDF: **31 trang**.
- Undefined citation/reference: **0**.
- Overfull box: **0**.
- Preflight: mở được, không mã hóa, không phải scan, không XFA.
- Render toàn bộ 31 trang ở 170 dpi.
- Kiểm tra trực quan các trang thay đổi chính:
  - H1--H2: trang 12;
  - H3: trang 16;
  - H4: trang 20;
  - H5: trang 21.
  Không còn clipping hoặc chồng chữ đáng kể.

### WP8-B supplement

`WP8_B_reproducibility_notation_supplement.pdf`:

- 3 trang landscape;
- không undefined/overfull sau bản build cuối;
- preflight sạch;
- render cả 3 trang và kiểm tra trực quan.

## 7. Việc còn lại sau Lượt B

Nội dung khoa học và hardening của WP8-B đã khóa. Lượt tiếp theo chỉ là **WP8.6 / Lượt C**:

1. tạo DOCX submission version;
2. reflow Hình 1--5 và Bảng 1--5 trong Word;
3. kiểm tra lại trạng thái nguồn pháp lý/dự thảo, DOI/URL đúng ngày nộp;
4. final submission preflight (claim, novelty boundary, figure/prose consistency, desk-format).

Không mở thêm contribution, scenario hoặc architecture decision mới trong Lượt C trừ khi preflight phát hiện lỗi thực chất.
