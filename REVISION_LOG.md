# REVISION_LOG

Nhật ký các work package (WP) áp dụng lên bản thảo VJST2. Mỗi mục ghi: vấn đề
được xử lý, file thay đổi, nội dung thêm/xóa chính, và số từ trước/sau.

---

## WP1 — Hệ thống hiện hữu và ranh giới kế thừa (2026-08-20)

### Vấn đề xử lý
Phản biện của bài trước ([2], code 4044) phê bình bản thảo không đề cập "Hệ
thống quản lý trực tuyến các nhiệm vụ khoa học và công nghệ" (stm.mst.gov.vn)
và không trả lời quan hệ với Nền tảng số quản lý KH,CN&ĐMST quốc gia (khoản 3
Điều 48 NĐ 268/2025/NĐ-CP). WP1 bổ sung phân tích định vị so với các hệ thống
đang vận hành/đã quy định và trả lời minh thị quan hệ với nền tảng quốc gia.

### File thay đổi

**03_background.tex** — thêm tiểu mục mới `2.3. Hệ thống hiện hữu và ranh giới
kế thừa` (`\label{subsec:existing-systems}`), đặt sau mục liên thông/quản trị
dữ liệu (2.2) và trước "Khoảng trống thiết kế" (nay chuyển thành 2.4). Nội dung:
- 5 đoạn văn (741 từ prose, đo bằng script bóc tách lệnh LaTeX): tổng quan 5 hệ
  thống hiện hữu; quan hệ với Nền tảng số quốc gia (dẫn Luật 93/2025/QH15 khoản
  3 Điều 20 và NĐ 268 khoản 3 Điều 48); xử lý thận trọng nguồn cho hệ thống quản
  lý trực tuyến nhiệm vụ KH&CN (stm.mst.gov.vn); ba hệ thống còn lại (TTHC, CSDL
  quốc gia về doanh nghiệp, CSDL chuyên ngành QĐ 1762); khoảng trống 5 điểm mà
  SRA đóng góp và nguyên tắc kế thừa/khác biệt hóa.
- Bảng mới `Bảng~\ref{tab:existing-systems}` (4 cột × 5 dòng): Hệ thống hiện hữu
  | Chức năng/dữ liệu đã phủ | Quan hệ với nền tảng đề xuất | Căn cứ. Đây trở
  thành Bảng 2 của bài (đánh số tự động qua `\ref`/`\caption`; các bảng sau đó
  tự dịch lên một số, ví dụ Bảng 6 (conformance) → Bảng 7, không cần sửa tay).
- wc -w thô (bao gồm mã LaTeX): 1172 → 2367 từ (+1195; phần lớn do bảng dài và
  các lệnh `\citep`/`\textbf` được đếm là từ).

**02_intro.tex** — thêm 3 câu vào đoạn nêu khoảng trống (cuối Mục 1), liệt kê 5
hệ thống hiện hữu, trỏ tới `subsec:existing-systems` và phát biểu trước kết
luận "thành phần chuyên ngành cấp Bộ, không phải hệ thống song song". wc -w thô:
1057 → 1181 (+124).

**07_interop.tex** — thêm 1 dòng vào bảng ranh giới liên thông (`tab:lienthong`,
nay là Bảng 5) cho biên với Nền tảng số quốc gia, đặt làm dòng đầu tiên (biên
vĩ mô nhất). wc -w thô: 1838 → 1921 (+83).

**09_discussion.tex** — nén Mục 8.2 (`subsec:design-principles`): gộp đoạn dẫn
nhập + ba đoạn đầy đủ P1/P2/P3 (297 từ prose) thành một đoạn dẫn nhập ngắn trỏ
về Mục 4.1–4.3 với P1/P2/P3 rút còn một mệnh đề mỗi nguyên tắc (186 từ prose;
-111 từ prose, -155 từ wc -w thô: 1752 → 1597). Bảng 6 (`tab:conformance-current`)
và đoạn nhận định sau bảng giữ nguyên như yêu cầu.

**references.tex** — thêm `\bibitem{luatkhcndmst2025}` (Luật KH,CN&ĐMST số
93/2025/QH15) và di chuyển `\bibitem{qd1762_2025}` từ cuối danh mục lên vị trí
mới, để giữ đúng quy ước "thứ tự bibitem theo lần xuất hiện đầu tiên trong thân
bài" (lần đầu xuất hiện nay là ở Mục 2.3 thay vì Mục 6 cũ). `refs.bib` không
cần sửa vì cả hai mục đã tồn tại sẵn.

### Số từ toàn bài (đo trên PDF biên dịch bằng `pdftotext | wc -w`)
- Trước WP1: 13754 từ, 29 trang.
- Sau WP1: 14921 từ, 30 trang.
- Biên dịch xelatex qua `latexmk`: không lỗi, không cảnh báo tham chiếu/trích
  dẫn thiếu (`Citation ... undefined`, `Reference ... undefined`), không
  overfull hbox.

### Điểm cần lưu ý / thiếu nguồn — CẦN NGƯỜI DÙNG BỔ SUNG
1. **Hệ thống quản lý trực tuyến nhiệm vụ KH&CN (stm.mst.gov.vn)**: nhóm tác giả
   KHÔNG tìm được văn bản pháp lý công khai (nghị định/quyết định/thông tư) mô
   tả chính thức phạm vi, đơn vị chủ quản, hoặc mốc mở rộng phạm vi dùng chung
   toàn Bộ mà đề bài WP1 nêu ("đã mở rộng phạm vi dùng chung toàn Bộ từ đầu
   2026"). Chi tiết này **không được đưa vào bản thảo** vì không có nguồn trích
   dẫn được — đúng theo ràng buộc "tuyệt đối không bịa ngày tháng/tên văn bản".
   Đoạn văn và dòng bảng tương ứng được đánh dấu `cần bổ sung`. Nếu có văn bản
   chính thức (quyết định phê duyệt hệ thống, thông báo mở rộng phạm vi, v.v.),
   xin cung cấp để nâng cấp từ mô tả thận trọng lên trích dẫn có căn cứ.
2. **Mục tiêu cắt 500–600 từ ở Mục 8.2**: chỉ đạt cắt 111 từ prose (~155 từ
   wc -w thô). Phần P1/P2/P3 sau khi loại bỏ đúng phần lặp lại nguyên vẹn với
   Mục 4.1–4.3 chỉ còn khoảng 297 từ gốc để cắt; cắt hết mức có thể mà không phá
   vỡ việc liệt kê ba nguyên tắc (vốn được 02_intro.tex viện dẫn) đã dùng hầu
   hết dư địa đó. Muốn cắt thêm 400–500 từ nữa sẽ phải động vào Mục 8.1, 8.3
   hoặc 8.4 (ngoài phạm vi "Mục 8.2" mà WP1 chỉ định) — chưa thực hiện, chờ xác
   nhận nếu người dùng muốn mở rộng phạm vi nén.
