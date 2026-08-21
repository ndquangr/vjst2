Bối cảnh: repo này chứa mã nguồn LaTeX của một bài báo nộp Tạp chí Khoa học và
Công nghệ Việt Nam (VJST), mảng Khoa học kỹ thuật và công nghệ, viết bằng tiếng
Việt. Chủ đề: kiến trúc tham chiếu phần mềm (SRA) cho nền tảng số quản lý doanh
nghiệp KH&CN và doanh nghiệp khởi nghiệp sáng tạo.

Cấu trúc: main.tex điều phối; 00_frontmatter, 01_abstract, 02_intro,
03_background, 04_method, 05_architecture, 06_data, 07_interop, 08_evaluation,
09_discussion, 10_conclusion; references.tex + refs.bib;
supplementary_material.tex; các artefact CSV; figure_sources/.

Ràng buộc bất di bất dịch cho MỌI thay đổi:
1. Nguyên tắc độc lập: bài này KHÔNG phải phần mở rộng của bài JSTPM trước
   ([2]). Không tái sử dụng yêu cầu chức năng, khung sáu lớp hay hình của bài đó
   để tổng hợp kiến trúc. [2] chỉ dùng để xác lập bối cảnh và ranh giới đóng góp.
2. Phân lớp nguồn A/D/M và phân mức căn cứ L1/L2/L3 là bất biến. Không bao giờ
   nâng nguồn lớp D (dự thảo) hoặc M (phương pháp/quốc tế) thành nghĩa vụ L1.
3. Không thêm số liệu định lượng về hiệu năng, độ trễ, tính sẵn sàng nếu chưa
   có phép đo. Không biến thời hạn nghiệp vụ (5/15/3 ngày) thành SLA kỹ thuật.
4. Không hạ mức các tuyên bố giới hạn hiện có. Bài phải giữ nguyên sự trung thực
   về việc đây là đánh giá trước triển khai.
5. Văn phong: tiếng Việt học thuật, câu trực tiếp, không marketing. Giữ đúng
   giọng hiện tại của bản thảo.

Quy trình làm việc:
- Mỗi work package làm trên một commit riêng, message dạng "WPn: <mô tả>".
- Sau mỗi WP, cập nhật REVISION_LOG.md: mục review nào được xử lý, file nào đổi,
  đoạn nào thêm/xóa, số từ tăng/giảm.
- Trước khi sửa, đọc file liên quan để nắm ngữ cảnh. Không sửa mù.
- Sau khi sửa, chạy compile main.tex kiểm tra không lỗi, và báo cáo số từ trước/sau.

Thư mục paper tham khảo: E:\OneDrive\NCS\My Papers\PlatformTSC\VJST2\papers (folder md cho đọc nội dung, pdf là văn bản gốc để rà soát khi cần)

---

## Trạng thái phiên làm việc hiện tại (2026-08-21)

Đang chạy liên tiếp `prompts/WP2-fix.md` rồi `prompts/WP3.md`, mỗi WP một commit riêng.

### WP2-fix — việc 1: ma trận EIF S7 thiếu ranh giới "Nền tảng số quốc gia"
Quyết định: chọn phương án **(b)** trong hai lựa chọn nêu ở WP2-fix.md — giữ
I1--I5 nguyên trạng, thêm **I6** cho ranh giới mới, bổ sung nhãn mã "(I<n>)"
ngay trong Bảng 5 thân bài (`tab:lienthong`, `07_interop.tex`) để lộ ánh xạ
thân bài--bổ trợ dù thứ tự mã không trùng thứ tự dòng.
Lý do chọn (b) thay vì (a) đổi số I1→I2...: (a) đòi hỏi sửa mọi tham chiếu
"I<n>" trong repo bao gồm `viewpoint_registry.csv` V6 ("Bảng 5/I1") mà ý
nghĩa "I1" ở đó chưa từng được xác nhận (câu hỏi mở từ WP2, xem REVISION_LOG
mục "Điểm cần lưu ý"); đổi số có nguy cơ lan sai số nếu suy luận nhầm hàng.
(b) là thay đổi cục bộ, an toàn hơn, đúng như người dùng đã nghiêng về.
Vị trí thêm hàng I6: **cuối bảng S7** (không chèn đầu bảng để khỏi đánh số
lại I1--I5) — chấp nhận thứ tự mã I6 xuất hiện sau I1--I5 dù ở thân bài dòng
"Nền tảng số quốc gia" đứng đầu Bảng 5.

### WP3 — chấm B0
B0 = phương án "kho tập trung đa tenant" của AD01 (một trong các alternatives
đã liệt kê sẵn trong `architecture_decisions.csv`), áp dụng **cùng lõi ổn
định đã tinh chỉnh** (AD01 write_scope/writer_epoch/máy trạng thái, AD03 cấu
hình có phiên bản/cửa sổ tương thích) như B1-R — CHỈ khác ở lựa chọn topology
(VP7): một kho tập trung thay vì kho vật lý tách biệt theo tỉnh (P-DIST).
Căn cứ: `architecture_elements.csv` AE24 ghi rõ "Kho vật lý tách biệt chỉ là
thuộc tính của P-DIST" — tức cơ chế single-active-writer là topology-độc lập.
README dòng "WP7.1" cũng xác nhận: "B0 chỉ là baseline contrast, không phải
ablation model."

Kết quả chấm B0 (10 kịch bản, lập luận đầy đủ trong
`evaluation_results_b0.csv`): **4 Trực tiếp (SC1,SC2,SC5,SC8), 4 Có điều kiện
(SC3,SC6,SC9,SC10), 2 Rủi ro kiến trúc (SC4,SC7)**. Không nghiêng có lợi cho
P-DIST: B0 tốt hơn B1-R ở 4 kịch bản (không cần mô hình đọc/hợp nhất liên
kho: SC5, SC8; không cần đồng bộ chéo kho cho SC9 dù vẫn giữ điều kiện; SC1/
SC2 topology-độc lập) và kém hơn ở đúng 2 kịch bản liên quan trực tiếp tới
cô lập miền sự cố (SC4, SC7) — đây là đánh đổi CỐ HỮU đã được ghi nhận sẵn
trong tradeoffs của AD01 ("P-DIST tăng cô lập miền sự cố"), không phải một
khoảng trống mới của lõi ổn định. Do đó KHÔNG dừng lại theo điều kiện "báo
cáo nếu B0 lộ khoảng trống mà B1-R chưa xử lý" — đây là thuộc tính đã biết
của lựa chọn VP7, không phải thiếu sót cần sửa AD.

### Tiến độ (cập nhật liên tục — xem lịch sử git/REVISION_LOG.md để biết chi tiết đã hoàn tất)
- [x] WP2-fix việc 1: S7 + Bảng 5 nhãn I-code (phương án b; sửa thêm 2 lỗi biên dịch tiền nhiệm phát hiện được: `\citep` không tồn tại trong supplementary, đường dẫn hình fig05→fig06)
- [x] WP2-fix việc 2: rút tóm tắt VI 233 từ, EN 163 từ (đo qua pdftotext), tương đương nội dung 1-1
- [x] WP2-fix: nghiệm thu (check_citation_order 37/37, compile main+supplementary sạch, 33tr/15885 từ) + REVISION_LOG — còn thiếu: commit
- [ ] WP3 việc 1-2: evaluation_results_b0.csv (10 dòng, có lập luận)
- [ ] WP3 việc 3: 08_evaluation.tex Bảng thành 4 cột B0|B1|B1-R|Hàm ý
- [ ] WP3 việc 4: viết lại Mục 7.3 dựa trên B0 thật, giữ cảnh báo không suy luận nhân quả
- [ ] WP3 việc 5: supplementary_material.tex S12 khớp (thêm cột B0)
- [ ] WP3: nghiệm thu + commit + REVISION_LOG
