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

> **Cập nhật:** cả hai điểm trên đã được xử lý bởi WP1-fix bên dưới — điểm 1
> bằng cách neo lại claim vào QĐ 1973 + QĐ 1762 (bỏ nhãn `cần bổ sung`), điểm 2
> bằng cách revert nguyên văn (xem WP1-fix, hạng mục 9).

---

## WP1-fix — Sửa mâu thuẫn SoR, phạm vi căn cứ pháp lý và thứ tự tài liệu tham khảo (2026-08-20)

### Vấn đề xử lý
Review WP1 phát hiện 9 lỗi/thiếu sót, trong đó 3 lỗi mức [Chặn]: (1) mâu thuẫn
về SoR — §2.3 phát biểu nền tảng/Bộ là SoR trong khi AD01 và Bảng thẩm quyền dữ
liệu ở 06_data.tex xác định SoR là NÚT TỈNH; (2) một dòng bảng ở 07_interop.tex
gộp sai hai nghĩa vụ pháp lý khác nhau (khoản 3 Điều 48 và khoản 2 Điều 66 NĐ
268) thành một, ngụ ý DN KNST cũng phải định kỳ cập nhật lên nền tảng quốc gia
— văn bản không quy định vậy; (3) cụm "nền tảng đề xuất ... có nghĩa vụ cập
nhật định kỳ" gán nghĩa vụ pháp lý L1 cho phần mềm thay vì cho UBND cấp tỉnh.
Ngoài ra: locator STT 38/43 bị đảo, thứ tự bibitem lệch, thiếu URL cho một mục
luật, thiếu liên kết tới điểm chẩn đoán C07, và Mục 8.2 (đã nén ở WP1) hóa ra
cần được revert vì P1/P2/P3 chính là phần design knowledge — đóng góp khoa học
— chứ không phải nội dung thừa.

### File thay đổi

**03_background.tex §2.3**
- [Chặn 1+3] Viết lại đoạn 2: SoR nay gắn đúng cho "nút tỉnh đang có quyết định
  công nhận/chứng nhận hiệu lực"; lớp trung ương của nền tảng và Nền tảng số
  quốc gia chỉ giữ vai trò đọc/tổng hợp. Nghĩa vụ cập nhật định kỳ (khoản 3 Điều
  48 NĐ 268) gắn cho UBND cấp tỉnh; nền tảng đề xuất được mô tả lại là "phương
  tiện kỹ thuật hỗ trợ", không phải chủ thể mang nghĩa vụ. Áp dụng tương tự cho
  ô bảng dòng "Nền tảng số quản lý KH,CN&ĐMST quốc gia" (bỏ cụm "nguồn ghi cấp
  Bộ").
- [Hạng mục 6] Đổi tên "hệ thống quản lý trực tuyến nhiệm vụ KH&CN" thành "Hệ
  thống quản lý nhiệm vụ KH&CN trực tuyến của Bộ" (nhất quán ở cả prose, bảng và
  02_intro.tex). Neo bằng hai căn cứ có văn bản: phạm vi dữ liệu giao dịch KH&CN
  theo QĐ 1973, và CSDL Nhiệm vụ khoa học và công nghệ (Cục Thông tin, Thống kê
  chủ trì) theo QĐ 1762 Phụ lục STT 43. Bỏ nhãn `\textsc{cần bổ sung}`; tên miền
  stm.mst.gov.vn giữ lại trong ngoặc như ví dụ vận hành, không phải căn cứ.
- [Hạng mục 5] Sửa locator đảo chiều: câu về ba hệ thống còn lại nay chỉ dẫn
  CSDL Doanh nghiệp khởi nghiệp với đúng locator STT 38 (CSDL Nhiệm vụ KH&CN đã
  chuyển sang đoạn về hệ thống quản lý nhiệm vụ, dùng STT 43 — không còn câu nào
  liệt kê cả hai STT cùng lúc nên không còn nguy cơ đảo thứ tự).
- [Hạng mục 7] Thêm 1 câu: danh mục QĐ 1762 chỉ đăng ký CSDL Doanh nghiệp khởi
  nghiệp, chưa có mục tương ứng cho DN KH&CN; đánh dấu `cần làm rõ`, dẫn chéo
  Mục S10.3 và S11 (C07) của tài liệu bổ trợ, không nâng thành xung đột.
- wc -w thô: 2367 → 2504 (+137).

**02_intro.tex** — đổi tên hệ thống cho khớp §2.3; tách rõ nghĩa vụ (UBND cấp
tỉnh) khỏi vai trò của nền tảng (kiến trúc hỗ trợ). wc -w thô: 1181 → 1196 (+15).

**07_interop.tex**
- [Chặn 1+2+3] Viết lại dòng "Nền tảng số quốc gia" trong `tab:lienthong`: tách
  hai nghĩa vụ (a) khoản 3 Điều 48 — định kỳ cập nhật Giấy chứng nhận DN KH&CN;
  (b) khoản 2 Điều 66 — thông báo Bộ trong 15 ngày, áp dụng cho cả Giấy công
  nhận (gồm DN KNST) và Giấy chứng nhận DN KH&CN — mỗi phát biểu có locator
  riêng; gán nghĩa vụ cho UBND cấp tỉnh, nền tảng chỉ là phương tiện kỹ thuật;
  bỏ "nguồn ghi cấp Bộ".
- [Hạng mục 9b] Nén đoạn mô tả P-DIST ở §6.4 (`subsec:v5v6`): bỏ phần lặp lại
  gần nguyên vẹn với §4.3 (`subsec:arch-decisions`) và §5.1 (`subsec:phanlopdulieu`
  trong 06_data.tex — "đa tenant, phân vùng logic/schema... kho vật lý theo
  tỉnh hoặc mô hình lai"); chỉ giữ phần thực sự mới: trỏ tới Hình~fig:pdist-main
  và mô tả hình cho thấy gì. 132 → 70 từ prose (-62).
- wc -w thô toàn file: 1921 → 1955 (+34, do dòng bảng dài hơn dù đoạn §6.4 đã cắt).

**09_discussion.tex**
- [Hạng mục 9] Revert nén Mục 8.2: khôi phục nguyên văn ba đoạn P1/P2/P3 có nhãn
  đậm như trước WP1, thêm một câu ngắn trỏ về Mục 4.1–4.3 vào cuối đoạn dẫn
  nhập (không có ở bản gốc trước WP1) để tránh lặp lập luận nền. 186 → 325 từ
  prose (+139).
- [Hạng mục 9a] Gộp hai dòng QĐ 3090 và QĐ 292 trong Bảng~`tab:conformance-current`
  (nay là Bảng 7) thành một dòng vì cùng loại lập luận "đặt trong hệ quy chiếu
  kiến trúc số quốc gia / kiểm tra theo mô hình tham chiếu"; giữ đủ hai trích
  dẫn, yêu cầu, bằng chứng và mục tham chiếu. 135 → 128 từ (-7).
- wc -w thô toàn file: 1597 → 1774 (+177).

**references.tex / refs.bib**
- [Hạng mục 8] Bổ sung URL và ngày truy cập cho `luatkhcndmst2025` (tìm được
  nguồn công khai: vanban.chinhphu.vn, docid=214603 — đã xác minh nội dung khớp
  Luật số 93/2025/QH15 qua WebFetch). Cập nhật đồng bộ ở `refs.bib`.
- [Hạng mục 4] Thứ tự bibitem: viết `scripts/check_citation_order.py` để quét
  toàn bộ `\cite*` theo đúng thứ tự `\input` trong `main.tex` và so với thứ tự
  `\bibitem` trong `references.tex`. Chạy lần đầu cho kết quả **37/37 khớp** —
  việc sửa lại nội dung §2.3 ở trên (đưa `qd1762_2025` STT 43 lên trước
  `luatdulieu2024` trong dòng đọc thực tế) đã tự khắc phục lệch thứ tự được nêu
  trong đề bài, nên KHÔNG cần đổi thủ công vị trí hai bibitem này thêm nữa.

**scripts/check_citation_order.py** (mới) — script Python độc lập, không phụ
thuộc gói ngoài; đọc `main.tex` để lấy thứ tự `\input`, quét `\cite*{...}` theo
thứ tự đó (kể cả trong bảng/hình vì mọi bảng dùng `[H]`), so với thứ tự
`\bibitem` trong `references.tex`. Thoát mã 0 nếu khớp hoàn toàn, mã 1 nếu lệch
và in danh sách vị trí lệch. Dùng lại như bước nghiệm thu bắt buộc mỗi WP sau.

### Nghiệm thu (theo đúng tiêu chí WP1-fix)
- `python scripts/check_citation_order.py` → **37/37 khớp**.
- `grep -r "nguồn ghi cấp Bộ" *.tex` → không còn kết quả.
- Mọi phát biểu "SoR" trong thân bài (03_background.tex, 06_data.tex) nay nhất
  quán: SoR = nút tỉnh đang có quyết định hiệu lực; trung ương/nền tảng quốc
  gia chỉ đọc/tổng hợp — khớp AD01 (05_architecture.tex) và
  `tab:masterdata` (06_data.tex).
- Biên dịch xelatex qua `latexmk`: không lỗi, không cảnh báo tham chiếu/trích
  dẫn thiếu, không overfull hbox.
- Số từ toàn bài (`pdftotext | wc -w`): 14921 → 15315 từ (+394); 30 → 32 trang.
  Đây là WP sửa lỗi đúng/sai, không phải WP kiểm soát độ dài; phần tăng chủ yếu
  đến từ việc revert Mục 8.2 (+139 từ prose) chỉ được bù một phần (-7 và -62 từ
  ở hai chỗ khác theo đúng hạng mục 9a/9b của đề bài) — xem ghi chú dưới.

### Điểm cần lưu ý — BÁO CÁO LẠI CHO NGƯỜI DÙNG
1. **Ngân sách độ dài của hạng mục 9 không cân bằng**: đề bài yêu cầu "bù ngân
   sách độ dài ở hai chỗ khác" cho việc revert Mục 8.2, nhưng phần nội dung thực
   sự trùng lặp có thể cắt ở Bảng 6/7 (gộp dòng QĐ 3090/QĐ 292) và ở §6.4
   07_interop.tex (đoạn P-DIST) chỉ cộng lại được -69 từ prose, trong khi revert
   thêm +139 từ. Đã cắt hết phần trùng lặp an toàn có thể cắt ở hai chỗ được chỉ
   định mà không lặp lại chính lỗi "xóa mất design knowledge" mà hạng mục 9 vừa
   yêu cầu sửa; không tự ý cắt thêm ở Mục 8.1/8.3/8.4 hoặc nơi khác vì ngoài
   phạm vi đề bài.
2. **URL cho `luatkhcndmst2025`**: đã tìm và xác minh qua WebFetch
   (vanban.chinhphu.vn/?pageid=27160&docid=214603, nội dung khớp Luật số
   93/2025/QH15, Quốc hội, 27/6/2025). Ghi ngày truy cập là 20/8/2026 (ngày thực
   hiện WP1-fix) thay vì tái dùng mốc "9/8/2026" của các nguồn khác trong corpus,
   vì đây là lần xác minh mới, không thuộc đợt rà soát gốc 08/08/2026.
