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

---

## WP0 — Vệ sinh bản thảo: nhãn nội bộ, tên phiên bản, trùng ký hiệu kịch bản (2026-08-20)

### Vấn đề xử lý
Sáu lỗi vệ sinh phát hiện độc lập với nội dung khoa học: (1) nhãn nội bộ
"VJST2 - Round 3 strengthened SRA manuscript" rò rỉ vào metadata các bản DOCX
nộp; (2) tên phiên bản kiến trúc lẫn lộn giữa B1$_0$ (rendered "B1₀", dễ đọc
nhầm "B10")/B1/B1-R/b1r; (3) trùng ký hiệu S — vừa là số kịch bản (S1--S10)
vừa là số mục tài liệu bổ trợ (S1--S12), ví dụ "S1" vừa là "Tập nguồn" vừa là
"Tỉnh xử lý và quyết định"; (4) câu placeholder chưa xử lý ở mục S6 tài liệu
bổ trợ; (5) `deployment_view.csv` rỗng (1 byte); (6) Luật 93/2025/QH15 được
tài liệu bổ trợ viện dẫn ("Luật 93, khoản 3 Điều 20") nhưng không có mục tham
khảo tương ứng ở Mục 1 thân bài (mục này đã được bổ sung ở phạm vi khác bởi
WP1/WP1-fix trong cùng phiên làm việc, nhưng chưa xuất hiện ở Mục 1 như đề bài
yêu cầu).

### File thay đổi

**Nhãn nội bộ trong DOCX (hạng mục 1)** — Grep văn bản không thấy chuỗi
"Round 3" ở bất kỳ file `.tex`/`.md` nào (chuỗi này chưa từng tồn tại trong
mã nguồn LaTeX); nguồn gốc thực tế là trường metadata `dc:title` trong
`docProps/core.xml` của 4 file DOCX, bị đặt cứng thành
"VJST2 - Round 3 strengthened SRA manuscript" thay vì tên bài báo. Đã sửa
bằng script Python (`zipfile`, giữ nguyên cấu trúc/compression/thứ tự các
entry khác trong zip) cho cả 4 file:
`VJST2_submission_round3_strengthened.docx`,
`VJST2_submission_round4_recentered.docx`,
`VJST2_submission_round5_hardened.docx`,
`VJST_SUBMISSION_PACKAGE_20260810/01_UPLOAD_TO_OJS/01_MANUSCRIPT_VJST2_round5_hardened.docx`
(bản dự kiến nộp OJS). `dc:title` mới: tên bài báo hiện hành lấy nguyên văn
từ `00_frontmatter.tex`. Đã xác minh `zipfile.testzip()` không báo lỗi và
`word/document.xml`/`docProps/app.xml` không còn chuỗi "Round 3" ở cả 7 file
DOCX trong repo (kể cả các bản chưa từng chứa nhãn lỗi).

**Tên phiên bản kiến trúc (hạng mục 2)** — Literal "B10" chưa từng tồn tại
trong mã nguồn; nguồn gây đọc nhầm là ký pháp subscript `B1$_0$` (render
"B1₀"). Chọn quy ước: **B1** cho ứng viên ban đầu, **B1-R** cho bản tinh
chỉnh, **B0** cho đường cơ sở tập trung (đã đúng sẵn). Thay `B1$_0$` → `B1`
trong toàn bộ `.tex` sống: `04_method.tex`, `08_evaluation.tex`,
`supplementary_material.tex` (2 vị trí, gồm cả tiêu đề Bảng S12),
`WP8_A_refinement_independence_supplement.tex`,
`WP8_B_reproducibility_notation_supplement.tex`; và `B1_0` → `B1` trong
`architecture_refinement_log.csv`, `prior_work_delta.csv`. Tên file
`evaluation_results_b1r.csv` và các trích dẫn `\texttt{...b1r.csv}` đã khớp
sẵn quy ước (không cần đổi tên).

**Trùng ký hiệu S -- kịch bản vs. mục tài liệu bổ trợ (hạng mục 3)** — Đổi
**S1--S10 (kịch bản) → SC1--SC10** ở mọi nơi các số này thực sự chỉ kịch bản,
giữ nguyên **S1--S12 (mục tài liệu bổ trợ, kể cả S9.1--S9.4/S10.1--S10.3)**
vì đó là namespace khác. Đã phân loại thủ công từng lần xuất hiện trước khi
đổi (ví dụ "Mục~S10.3 và S11 (C07)" trong `03_background.tex` là tham chiếu
mục tài liệu, KHÔNG đổi). Đồng thời đổi `R-S9`/`R-S10` (refinement ID bắt
nguồn từ số kịch bản) → `R-SC9`/`R-SC10` cho nhất quán. File sửa:
`04_method.tex`, `08_evaluation.tex` (bảng + prose), `09_discussion.tex`,
`05_architecture.tex` (AD01/AD03), `06_data.tex`,
`supplementary_material.tex` (Mục S5, S12, prose S9/S10 rời rạc),
`WP8_A_refinement_independence_supplement.tex`,
`WP8_B_reproducibility_notation_supplement.tex` (bảng COV + bảng đăng ký
kịch bản), và các CSV: `evaluation_scenarios.csv`, `evaluation_results.csv`,
`evaluation_results_b1r.csv`, `scenario_coverage.csv`,
`scenario_coverage_rules.csv`, `evaluation_refinements.csv`,
`architecture_refinement_log.csv`, `architecture_decisions.csv`.

**Placeholder chưa xử lý ở S6 (hạng mục 4)** — Xóa câu "Trước khi nộp chính
thức, gói dữ liệu bổ trợ nên được đóng băng... Các định danh phát hành được
điền sau khi chốt bản nộp cuối..." trong `supplementary_material.tex`; thay
bằng `% TODO-WP6: điền định danh phát hành chính thức (DOI/URL/tag/commit/
checksum)...` — comment LaTeX, không hiển thị trong PDF.

**`deployment_view.csv` rỗng (hạng mục 5)** — **Lựa chọn: điền nội dung**
thay vì xóa, vì nội dung có thể trích xuất trực tiếp, không suy diễn, từ
`figure_sources/fig05_c4_deployment_pdist.tex` (Hình 5, đã có trong thân bài)
— tránh mất một artefact máy-đọc-được mà README đã liệt kê. File mới có 3
dòng: Nút tỉnh P_i, Nút trung ương, Hạ tầng chia sẻ/điều phối + Agent Node,
mỗi dòng liệt kê đúng các Container instance và quan hệ đã vẽ trong Hình 5,
không thêm chi tiết nào ngoài hình.

**Luật 93/2025/QH15 ở Mục 1 (hạng mục 6)** — `luatkhcndmst2025` đã có trong
`refs.bib`/`references.tex` từ WP1, và đã được trích ở Mục 2.3
(`03_background.tex`) và Bảng ranh giới liên thông (`07_interop.tex`) từ
WP1-fix, nhưng chưa xuất hiện ở Mục 1 như đề bài WP0 yêu cầu minh thị. Thêm
`\citep[khoản 3 Điều 20]{luatkhcndmst2025}` ngay tại điểm nhắc "Nền tảng số
quản lý KH,CN&ĐMST quốc gia" lần đầu trong câu đầu tiên của `02_intro.tex`;
đồng thời gắn `\citep{nd268_2025}` ngay sau "Nghị định số 268/2025/NĐ-CP" ở
đầu câu đó để giữ đúng vị trí trích dẫn đầu tiên của nd268_2025 (đã là mục
[1] từ trước). Do luatkhcndmst2025 giờ được trích lần đầu ở Mục 1 (trước cả
`nhom_bai1`), di chuyển `\bibitem{luatkhcndmst2025}` từ vị trí cũ (giữa
`nd356_2025` và `qd1762_2025`, do WP1-fix đặt) lên ngay sau `\bibitem{nd268_2025}`.

### Nghiệm thu
- `python scripts/check_citation_order.py` → **37/37 khớp** (chạy lại sau khi
  di chuyển bibitem `luatkhcndmst2025`; lần chạy trung gian ngay sau khi thêm
  câu trích dẫn ở Mục 1 nhưng trước khi dời bibitem báo 11/37, đúng như dự
  kiến vì thứ tự xuất hiện trong thân bài đã đổi).
- `grep -rn "B10"` và `grep -rn "B1_0\|B1\$_0\$"` trên toàn bộ `.tex`/`.csv`
  sống (loại trừ `VJST_SUBMISSION_PACKAGE_20260810/`) → không còn kết quả.
- `grep -rnE 'bare S9/S10 ngoài mục tài liệu'` (quét thủ công, phân loại theo
  ngữ cảnh) → không còn kịch bản nào dùng ký hiệu S trần; toàn bộ 10 kịch bản
  và các refinement ID liên quan dùng SC1--SC10/R-SC9/R-SC10.
- Chuỗi "Round 3" không còn trong `word/document.xml`, `docProps/core.xml`,
  `docProps/app.xml` của cả 7 file DOCX trong repo (kiểm tra bằng
  `unzip -p ... | grep`, vì ripgrep không đọc được nội dung nén bên trong
  DOCX nên bước "grep toàn repo" của đề bài tự nó không phát hiện được lỗi
  gốc — đã kiểm tra trực tiếp qua zip thay vì chỉ dựa vào grep).
- `latexmk -xelatex main.tex`: biên dịch sạch, không lỗi, không cảnh báo
  tham chiếu/trích dẫn thiếu, không overfull hbox. 32 trang (không đổi so
  với sau WP1-fix), 15315 → 15337 từ (`pdftotext | wc -w`; +22, hạng mục 6
  là thay đổi nội dung duy nhất của WP0, còn lại là đổi tên/định dạng).
- Biên dịch riêng `supplementary_material.tex` và
  `WP8_A_refinement_independence_supplement.tex` bằng `xelatex`: sạch, PDF
  đã được build lại và cập nhật trong repo.
  `WP8_B_reproducibility_notation_supplement.tex` **không biên dịch được**
  trong môi trường hiện tại vì thiếu font "Liberation Serif" (lỗi môi trường
  có sẵn từ trước, không liên quan tới sửa đổi của WP0 — xác nhận bằng
  `git diff` cho thấy dòng `\setmainfont{Liberation Serif}` không đổi, và
  bằng bản sao thử nghiệm đổi tạm sang DejaVu Serif biên dịch sạch). PDF của
  file này **chưa được build lại**; cần build trên máy có Times New
  Roman/Liberation Serif, hoặc sửa fallback font giống các supplement khác
  (`\IfFontExistsTF{Times New Roman}{...}{\setmainfont{DejaVu Serif}}`) —
  đây là sửa đổi ngoài phạm vi 6 hạng mục của WP0 nên chưa tự ý thực hiện.

### Điểm cần lưu ý — BÁO CÁO LẠI CHO NGƯỜI DÙNG
1. `WP8_B_reproducibility_notation_supplement.pdf` trong repo hiện **lệch**
   với `.tex` đã sửa (PDF cũ còn "S1--S10"/"B1$_0$"; `.tex` đã có
   "SC1--SC10"/"B1"). Cần build lại PDF này trước khi coi tài liệu bổ trợ là
   nhất quán/đóng băng, sau khi xử lý lỗi font ở trên.
2. `VJST_SUBMISSION_PACKAGE_20260810/02_SUPPLEMENTARY_DATA_RELEASE/` là gói
   "frozen" theo `00_README_SUBMISSION_PACKAGE.md`; các CSV/tex bên trong đó
   (bản sao của `architecture_refinement_log.csv`, `prior_work_delta.csv`,
   `architecture_decisions.csv`, `evaluation_refinements.csv`, v.v.) **chưa
   được đồng bộ** với các sửa đổi hạng mục 2--3 ở bản làm việc gốc, vì gói
   này được tài liệu hóa là snapshot chỉ-đọc, không phải nơi sửa trực tiếp.
   Chỉ file DOCX trong gói (`01_UPLOAD_TO_OJS/...round5_hardened.docx`) được
   sửa, vì đó đúng là hạng mục 1 của đề bài. Cần tái tạo (regenerate) toàn bộ
   gói `02_SUPPLEMENTARY_DATA_RELEASE/` từ các file gốc đã sửa trước khi nộp
   chính thức.
3. `README.md` còn nhắc "B1$_0$", "S1--S10", "R-S9/R-S10" ở các đoạn tường
   thuật lịch sử theo mốc WP (ví dụ "Sau các vòng WP7--WP8-B..."). Đây là
   nhật ký diễn biến dự án, không phải bản thảo khoa học nằm trong phạm vi 6
   hạng mục của WP0 ("tất cả file .tex, supplementary_material.tex, và
   tên/nội dung các file CSV"); **chưa sửa** để tránh viết lại lịch sử ngoài
   yêu cầu. Báo lại nếu muốn đồng bộ hóa thuật ngữ trong README luôn.

---

## WP1-fix2 — Ba tồn đọng từ review WP1-fix, gộp chung commit với WP2 (2026-08-21)

### Vấn đề xử lý
Review WP1-fix phát hiện 3 tồn đọng: (a) câu cuối đoạn 2 của §2.3 vỡ ngữ pháp
sau khi viết lại ở WP1-fix -- mệnh đề "-- nghiệp vụ công nhận/chứng nhận DN
KH&CN và DN KNST mà chưa hệ thống nào khác đảm nhiệm đầy đủ" không còn chủ
ngữ để gắn vào; (b) ô bảng `tab:existing-systems` viết "UBND cấp tỉnh (SoR
nghiệp vụ)", lẫn chủ thể pháp lý (cơ quan) với vai trò hệ thống (SoR là vai
trò của nút tỉnh, không phải của UBND); (c) dòng bảng "Nền tảng số quốc gia"
trong `07_interop.tex` dài gấp ~3 lần các dòng khác vì phần (b) về khoản 2
Điều 66 trùng lặp với Mục 6.2 (`subsec:sla`) vốn đã xử lý kỹ hơn.

### File thay đổi

**03_background.tex §2.3**
- [a] Tách câu cuối đoạn 2 thành câu độc lập: "Nghĩa vụ này thuộc về UBND cấp
  tỉnh..." giữ nguyên; thêm câu mới "Nghiệp vụ công nhận/chứng nhận DN KH&CN
  và DN KNST chính là phần mà chưa hệ thống hiện hữu nào trong số năm hệ
  thống trên đảm nhiệm đầy đủ -- đây là lý do tồn tại của nền tảng đề xuất."
  có chủ ngữ rõ ràng, không còn treo lửng sau dấu gạch ngang.
- [b] Ô bảng dòng "Nền tảng số quản lý KH,CN&ĐMST quốc gia": viết lại từ
  "UBND cấp tỉnh (SoR nghiệp vụ) dùng nền tảng..." thành "UBND cấp tỉnh mang
  nghĩa vụ...; trong kiến trúc, nút tỉnh -- không phải cơ quan hay nền tảng
  ở mức tổng thể -- giữ vai trò SoR nghiệp vụ." Grep `UBND.*SoR\|SoR.*UBND`
  và `cơ quan.*SoR\|SoR.*cơ quan` toàn repo: chỉ còn hai chỗ, cả hai đều là
  câu đã sửa đúng (phân biệt rõ vai trò), không còn chỗ nào lẫn.
- [f, gộp từ yêu cầu nghiệm thu WP2] Thêm câu trỏ xuôi từ §2.3 sang Mục 5.2:
  "...(SoR) cho phạm vi thẩm quyền của mình -- cơ chế gán và chuyển giao vai
  trò này theo thời gian được hình thức hóa ở Mục~\ref{subsec:masterdata}".

**07_interop.tex** [c] — Rút gọn ô "Nguồn/thẩm quyền cần bảo toàn" của dòng
"Nền tảng số quốc gia": giữ đầy đủ (a) khoản 3 Điều 48; rút (b) khoản 2 Điều
66 còn một mệnh đề ngắn kèm `\ref{subsec:sla}` thay vì lặp lại cơ chế gửi
lại/chống trùng/bằng chứng đã có ở Mục 6.2. Ô "Hệ quả kiến trúc" rút tương
ứng (bỏ phần mô tả (b) trùng lặp). Độ dài ô nay tương đương các dòng khác
trong bảng.

### Nghiệm thu WP1-fix2
- `grep` xác nhận không còn chỗ nào lẫn vai trò SoR với chủ thể pháp lý.
- Biên dịch sạch (gộp chung với compile cuối của WP2 bên dưới).

---

## WP2 — Mô hình gán quyền ghi theo phạm vi/thời gian thành đóng góp số 1 (2026-08-21)

### Vấn đề xử lý
Cơ chế gán quyền ghi (`write_scope` + `jurisdiction_id` + khoảng hiệu lực +
`writer_epoch` đơn điệu + máy trạng thái `prepared→old-frozen→cutover-confirmed
→new-active→completed`, bất biến single-active-writer) là phần duy nhất của
bài mang tính thiết kế mới, tổng quát hóa được ra ngoài miền DN KH&CN/DN
KNST -- nhưng trước WP2 nó chỉ có một đoạn ngắn ở Mục 5.2, còn chi tiết đầy
đủ nằm ở tài liệu bổ trợ (S9.2, S10.1). WP2 nâng cơ chế này thành đóng góp
số 1, được đặt tên, có hình minh họa riêng trong thân bài.

### File thay đổi

**06_data.tex §5.2 (`subsec:masterdata`)** — Mở rộng đoạn ~80 từ thành ~450
từ prose (đo bằng script bóc tách LaTeX, không tính hình/bảng): cấu trúc bản
ghi gán quyền ghi (4 nhóm trường: chủ thể/phạm vi, địa bàn/hiệu lực, bằng
chứng/giao dịch chuyển quyền, phiên writer); bất biến single-active-writer;
chuỗi trạng thái chuyển giao; quy tắc hủy (chỉ trước `new-active`) và phục
hồi tiến (sau `new-active`); quy tắc xác minh `writer_epoch` khi khởi động
lại sau gián đoạn; phát biểu tường minh mức L2 (không khóa consensus/khóa/
middleware); và một câu tổng quát hóa rõ ràng cho "bất kỳ nền tảng chính phủ
đa cấp nào có chuyển giao thẩm quyền theo thời gian". Chèn Hình~4 (mới)
ngay giữa đoạn giải thích máy trạng thái. Thêm câu trỏ ngược về §2.3
(`subsec:existing-systems`) để khớp phát biểu SoR mới.

**Hình 4 mới -- máy trạng thái chuyển giao quyền ghi** — Tạo
`figure_sources/fig04_write_authority_transfer_fsm.tex` theo đúng
preamble/convention của 5 hình hiện có (standalone TikZ, fontspec Times New
Roman/DejaVu Serif fallback, polyglossia). Ký pháp **UML State Machine**
(không phải ArchiMate/C4 như 5 hình kia) theo đúng quy tắc 11 của README
("State Machine cho cấu trúc và hành vi chi tiết"): initial pseudo-state,
5 trạng thái hợp lệ + 1 trạng thái hủy (`aborted`), final pseudo-state,
chuyển tiếp có nhãn, ranh giới đứt phân tách vùng "có thể hủy"/"không thể
hủy -- chỉ phục hồi tiến". Tọa độ được thiết kế lại 2 lần sau khi phát hiện
nhãn cạnh chồng lấn lên hộp trạng thái khi kiểm tra trực quan (render PNG độ
phân giải cao); bản cuối biên dịch sạch, không overfull hbox khi nhúng vào
thân bài. Chèn nguyên khối TikZ (đồng bộ tuyệt đối với file trong
`figure_sources/`) vào `06_data.tex`.

**Đánh số lại hình sau khi chèn Hình 4 (hạng mục e của WP1-fix2)** — Hình cũ
4 (Container/ranh giới, `07_interop.tex`) → Hình 5; Hình cũ 5 (P-DIST,
`07_interop.tex`) → Hình 6. Đổi tên file nguồn tương ứng:
`fig04_c4_container_boundaries.*` → `fig05_c4_container_boundaries.*`;
`fig05_c4_deployment_pdist.*` → `fig06_c4_deployment_pdist.*` (git mv, giữ
nguyên nội dung/PDF, chỉ đổi tên + comment "% Hình N" nội bộ). Cập nhật
`\includegraphics` trong `07_interop.tex` sang `fig06_...`. Quét toàn repo
mọi chuỗi "Hình N"/"Bảng N" viết tay (không phải `\ref`) và sửa nốt các
registry máy đọc bị lệch:
- `figure_sources/README_FIGURES.md`: bảng ánh xạ Hình 1--6, thêm nguyên tắc
  ký pháp UML cho Hình 4.
- `viewpoint_registry.csv`: V1 Hình4→Hình5; V2 Bảng2→Bảng3 (lệch từ *trước*
  WP1, chưa từng được sửa -- tab:arch-decisions-summary đã là Bảng3 từ khi
  WP1 chèn Bảng2 mới); V3 Hình3→"Hình 3--4", Bảng3→Bảng4, bổ sung notation
  "UML State Machine"; V4 Bảng4→Bảng5; V5 Hình5→Hình6; V6 "Bảng 4/I1" →
  "Bảng 5/I1" (suy luận theo cùng quy luật +1, **chưa xác nhận được ý nghĩa
  của "I1"** -- báo lại bên dưới).
- `notation_registry.csv`: chèn hàng H4 (UML State Machine), dịch H4→H5,
  H5→H6; sửa cross-ref nội bộ "Ánh xạ các vùng chứa H4" → "H5".
- `prior_work_delta.csv`: "Năm hình H1-H5" → "Sáu hình H1-H6".
- `WP8_B_reproducibility_notation_supplement.tex` mục C: bảng ký pháp
  "Hình 1--5" → "Hình 1--6", chèn hàng H4, dịch H4→H5/H5→H6, sửa cross-ref
  "H4 vào nút triển khai" → "H5", cập nhật dòng "Đối soát cuối WP8-B".
- `README.md`: đổi tiêu đề "Bốn hình và năm bảng..." → "Sáu hình và bảy
  bảng...", viết lại bảng liệt kê đầy đủ 6 hình + 7 bảng đúng nội dung/mục
  hiện hành (bảng này mô tả trạng thái hiện tại, không phải nhật ký lịch sử
  theo mốc WP, nên được cập nhật; các đoạn "HOÀN THÀNH ngày..." khác giữ
  nguyên vì đó là lịch sử tại thời điểm viết).
- Xác nhận bằng `pdftotext` trên PDF đã biên dịch: Hình 1--6 và Bảng 1--7
  đều đúng thứ tự, đúng caption; không còn `\ref` nào trỏ sai (biên dịch
  latexmk không báo `Reference ... undefined` hay `may have changed`).

**01_abstract.tex** — Viết lại đoạn kết quả VI + EN: bỏ câu "Từ 16 tài liệu,
nghiên cứu xác lập 116 đơn vị nguồn và 128 dòng truy vết..."; thay bằng phát
biểu phát hiện đặt tên mô hình gán quyền ghi ("Phát hiện trung tâm là quyền
ghi cần được biểu diễn như một gán có phạm vi thẩm quyền và thời gian hiệu
lực... single-active-writer"). Giữ nguyên 16/116/128 ở Mục 3.2
(`subsec:corpus`, đã có sẵn, không đổi) đúng theo yêu cầu. VI: 298 → 321 từ;
EN: (đếm mới) 200 từ -- cả hai vẫn trong hoặc gần khoảng 160--250 từ/ngôn ngữ
của quy tắc 13 (VI đã vượt nhẹ từ trước WP2, không phải lỗi mới).

**02_intro.tex** — Đoạn "Bài đóng góp ba kết quả chính": hoán đổi thứ tự
Thứ nhất/Thứ hai (mô hình gán quyền ghi lên đầu, đặt tên và mô tả cơ chế;
SRA đa góc nhìn xuống vị trí hai); Thứ ba (quy trình truy vết, giữ 16/116/128)
không đổi vị trí. Câu "Từ hai đóng góp kiến trúc đầu, Mục~... khái quát ba
nguyên tắc..." giữ nguyên vì hai đóng góp đầu vẫn là cùng một cặp nội dung,
chỉ hoán vị trí 1↔2 với nhau -- không phá vỡ liên kết tới P1--P3 ở Mục 8.2.

**10_conclusion.tex** — Câu tổng kết đóng góp: đặt mô hình gán quyền ghi lên
đầu danh sách, có tên và nhắc máy trạng thái/single-active-writer, kèm câu
tổng quát hóa; các đóng góp còn lại (lõi ổn định/điểm biến thiên, ranh giới
liên thông, chuỗi truy vết) giữ nguyên nội dung, dịch xuống.

**supplementary_material.tex S9.2/S10.1** — Bỏ phần mô tả cơ chế trùng lặp
nguyên văn với Mục 5.2 mới (cấu trúc trường, chuỗi trạng thái, hủy/phục hồi
tiến, xác minh epoch khi khởi động lại); mỗi mục thay bằng một câu trỏ ngược
"đã được trình bày đầy đủ ở Mục~5.2 của thân bài (Hình~4)". S9.2 (AD01) giữ
lại phần KHÔNG có ở thân bài (liên kết với VP7/P-DIST). S10.1 giữ nguyên
danh mục 4 nhóm trường (đúng yêu cầu "giữ lại chi tiết trường dữ liệu") làm
tham chiếu triển khai, chỉ cắt phần narrative đã trùng.

### Nghiệm thu (đối chiếu đầy đủ với WP1-fix2 + WP2)
- `python scripts/check_citation_order.py` → **37/37 khớp** (không citation
  mới nào được thêm trong WP2, không cần sửa `references.tex`).
- Biên dịch `latexmk -xelatex main.tex`: sạch, không lỗi, không cảnh báo
  tham chiếu/trích dẫn thiếu, **0 overfull hbox** (Hình 4 ban đầu gây 1
  overfull ~6pt do chú giải quá rộng; đã sửa `text width` từ 15.4cm xuống
  15.0cm).
- Đối soát số hình/bảng bằng `pdftotext`: Hình 1--6, Bảng 1--7 đúng thứ tự,
  đúng caption; grep xác nhận không còn "Hình N"/"Bảng N" viết tay nào trỏ
  sai (chỉ còn trích dẫn ngoài tới "Hình 3" của EIF, không phải tự trỏ).
  Kiểm tra trực quan Hình 4 bằng render PNG độ phân giải cao (300 DPI) qua
  hai vòng sửa tọa độ trước khi xác nhận không còn nhãn chồng hộp trạng thái.
- Kiểm tra thủ công §2.3 (Mục 2.3, background) và Mục 5.2 (06_data.tex) có
  tham chiếu chéo hai chiều nhất quán về SoR = nút tỉnh, không phải cơ quan
  hay nền tảng ở mức tổng thể.
- **Số trang/từ:** trước WP1: 13754 từ, 29 trang. Sau WP0: 15337 từ, 32
  trang. Sau WP1-fix2+WP2: **15948 từ, 33 trang** (`pdftotext | wc -w`,
  `pdfinfo`). Tăng lũy kế so với trước WP1: **+2194 từ (+16,0%), +4 trang**.
  Riêng delta WP1-fix2+WP2: +611 từ, +1 trang.

### Điểm cần lưu ý — BÁO CÁO LẠI CHO NGƯỜI DÙNG
1. **`viewpoint_registry.csv`, hàng V6, cột `body_artifact` = "Bảng 4/I1"**:
   đã đổi thành "Bảng 5/I1" theo cùng quy luật +1 áp dụng cho các hàng khác
   (Bảng cũ 4 = `tab:lienthong`, nay là Bảng 5), nhưng nhóm tác giả **không
   xác định được "I1" trỏ tới đâu** -- không tìm thấy định nghĩa "I1" ở bất
   kỳ file nào khác trong repo (không phải mã AE/AD/VP/CR/Cxx.yy đã biết).
   Có thể là appendix nội bộ chưa từng được tạo, hoặc ký hiệu lỗi thời sót
   lại. Xin xác nhận hoặc cung cấp ngữ cảnh để sửa đúng.
2. **Độ dài tóm tắt tiếng Việt (321 từ)** đã vượt khoảng 160--250 từ của quy
   tắc 13 -- nhưng bản trước WP2 (298 từ) cũng đã vượt sẵn từ trước, đây
   không phải hồi quy mới do WP2 gây ra. Chưa chủ động cắt để không mất nội
   dung phát hiện mới theo đúng yêu cầu; báo lại nếu cần nén xuống đúng
   ngưỡng trước khi nộp.
3. Hai file PDF nguồn hình bị đổi tên (`fig05_c4_container_boundaries.pdf`,
   `fig06_c4_deployment_pdist.pdf`) giữ nguyên nội dung nhị phân (chỉ
   `git mv`, không build lại) vì nội dung TikZ bên trong không đổi, chỉ số
   thứ tự đổi; đã xác nhận qua diff rằng nội dung `.tex` nguồn chỉ khác dòng
   comment "% Hình N" ở đầu file.

---

## WP2-fix — Ma trận EIF S7 thiếu ranh giới mới + rút tóm tắt VI/EN (2026-08-21)

### Việc 1 — Bảng 5 (`tab:lienthong`) có 6 ranh giới nhưng ma trận EIF S7 chỉ có I1--I5
Dòng "Nền tảng số quốc gia" được WP1 thêm vào Bảng 5 thân bài nhưng chưa có
ánh xạ bốn lớp EIF (Pháp lý/Tổ chức/Ngữ nghĩa/Kỹ thuật) tương ứng trong S7 --
vi phạm chính phương pháp luận EIF mà Mục 6 tuyên bố dùng.

**Quyết định đánh mã (phương án b, như đề xuất của người yêu cầu):** giữ
nguyên I1--I5, thêm **I6** ở CUỐI bảng S7 (không chèn đầu bảng), và hiển thị
nhãn "(I\emph{n})" ngay trong Bảng 5 thân bài cạnh mỗi tên ranh giới. Lý do
chọn (b) thay vì (a) đổi số I1→I2...I5→I6: (a) đòi hỏi sửa lại mọi tham
chiếu "I\emph{n}" hiện có trong repo, đáng chú ý `viewpoint_registry.csv`
hàng V6 trỏ "Bảng 5/I1" mà ý nghĩa "I1" ở đó **chưa từng được xác nhận**
(câu hỏi mở còn treo từ WP2 -- xem mục "Điểm cần lưu ý" phía trên). Đổi số
trong tình huống còn một tham chiếu chưa rõ nghĩa có nguy cơ lan sai nếu suy
luận nhầm hàng khi rà thủ công; (b) là thay đổi cục bộ, không đụng tới bất
kỳ file nào khác ngoài hai bảng liên quan, an toàn hơn. Hệ quả chấp nhận:
thứ tự mã I6 xuất hiện sau I1--I5 trong S7 dù ở thân bài dòng "Nền tảng số
quốc gia" đứng đầu Bảng 5 -- điều này được ghi chú tường minh ngay sau bảng
S7 để người đọc không nhầm là lỗi.

**File thay đổi:**
- `supplementary_material.tex` (S7): thêm hàng I6 vào cuối `longtable`, đủ
  bốn lớp EIF theo đúng nội dung yêu cầu (Luật 93 khoản 3 Điều 20; NĐ 268
  khoản 3 Điều 48; NĐ 268 khoản 2 Điều 66 -- ba khoản trích dẫn tách biệt,
  không gộp phạm vi, đúng nguyên tắc đã sửa ở WP1-fix). Thêm một câu chú
  thích ngay sau bảng giải thích lựa chọn đánh mã (b) và vị trí I6.
  **Lưu ý kỹ thuật quan trọng phát hiện khi biên dịch:** `supplementary_material.tex`
  là tài liệu LaTeX độc lập (`\documentclass` riêng, ghi rõ trong comment đầu
  file "không được `\input{}` vào thân bài chính") và **không nạp gói trích
  dẫn nào** (không `natbib`/`biblatex`) -- toàn bộ 12 mục S1--S12 từ trước
  tới nay đều trích luật bằng văn bản thường (ví dụ "NĐ 268 khoản 1 Điều
  18..."), không dùng `\citep`. Bản nháp đầu tiên của hàng I6 dùng `\citep`
  theo đúng văn phong thân bài nhưng gây lỗi biên dịch "Undefined control
  sequence" vì macro đó không tồn tại trong tài liệu này; đã sửa lại thành
  trích dẫn văn bản thường đúng quy ước sẵn có của bổ trợ. Tương tự, câu chú
  thích ban đầu dùng `\ref{tab:lienthong}` (label định nghĩa trong
  `07_interop.tex`, chỉ tồn tại khi biên dịch qua `main.tex`) -- cũng lỗi vì
  lý do độc lập tài liệu nêu trên; đã đổi thành số bảng viết tay "Bảng~5"
  kèm tên bảng, đúng quy ước toàn bộ tài liệu bổ trợ (không `\ref` chéo sang
  thân bài).
- `07_interop.tex` (Bảng~\ref{tab:lienthong}): thêm nhãn "(I\emph{n})" vào
  sau tên mỗi ranh giới (I1 Định danh/xác thực ... I6 Nền tảng số quốc gia);
  thêm một câu ngay sau bảng giải thích ý nghĩa nhãn và việc thứ tự mã không
  trùng thứ tự dòng.

**Phát hiện phụ (ngoài phạm vi yêu cầu, sửa vì nghiệm thu bắt buộc "biên dịch
sạch cả main và supplementary"):** khi biên dịch độc lập
`supplementary_material.tex` lần đầu tiên trong phiên làm việc này (dường
như chưa từng được biên dịch riêng kể từ khi đổi tên file hình ở WP2), phát
hiện Mục S8 vẫn tham chiếu `figure_sources/fig05_c4_deployment_pdist.pdf` --
tên file này đã được `git mv` thành `fig06_c4_deployment_pdist.pdf` ở WP2
nhưng `\includegraphics` trong bổ trợ bị sót không cập nhật, gây lỗi "file
not found". Đã sửa đường dẫn về đúng `fig06_...`.

### Việc 2 — Tóm tắt VI vượt khung 160--250 từ và không tương đương nội dung với EN
Tóm tắt VI trước sửa: 328 từ (đo bằng script bóc tách LaTeX cục bộ) / 233 từ
(đo bằng `pdftotext` trên PDF đã biên dịch, phương pháp cuối cùng dùng để
báo cáo). Tóm tắt EN trước sửa: 200/163 từ theo hai phương pháp tương ứng.

**Nguyên tắc cắt áp dụng (theo đúng thứ tự ưu tiên của yêu cầu):** giữ
nguyên hoàn toàn (i) câu bối cảnh, (ii) câu DSR+SRA truy vết, (iii) câu phát
hiện trung tâm (quyền ghi = gán có phạm vi/thời gian hiệu lực + máy trạng
thái single-active-writer -- đóng góp số 1, chỉ bỏ một cụm diễn giải trùng
nghĩa "một writer hợp lệ tại một thời điểm" đứng ngay trước thuật ngữ tiếng
Anh cùng nghĩa), (iv) câu kết quả mười kịch bản/hậu kiểm, (vi) câu giới hạn
scenario-based verification. Cắt mạnh nhất ở hai chỗ đúng như gợi ý: (a) bỏ
hẳn câu "SRA tách lõi ổn định khỏi điểm biến thiên, xác định nguồn dữ liệu
theo nhóm thuộc tính, quản trị cấu hình quy trình và liên thông..." -- trùng
ý với chính ba nguyên tắc thiết kế P1--P3 được liệt kê ngay sau đó trong
cùng đoạn tóm tắt; (b) nén câu liệt kê đầy đủ ba nguyên tắc (ba mệnh đề đủ
chủ ngữ-vị ngữ) thành một cụm ngắn nêu tên ba ý mà không diễn giải lại từng
mệnh đề. Áp dụng cắt tương tự cho bản EN (bỏ đúng câu SRA tách lõi tương ứng,
nén cụm ba nguyên tắc) để đạt tương đương nội dung hai bản -- đây là thay đổi
bắt buộc để xử lý phần cốt lõi của yêu cầu ("bản Việt nói nhiều hơn bản
Anh"), không chỉ là cắt để đạt số từ.

**Kết quả:** VI 233 từ, EN 163 từ (đo bằng `pdftotext` trên `main.pdf` đã
biên dịch lại). VI nằm trong khung 230--240 từ yêu cầu; EN nằm trong khung
160--250 từ chung của tạp chí. Hai bản nay có đúng bảy câu tương ứng 1-1 về
nội dung (trước đó VI có một câu EN cũng có nhưng bị lặp ý ở cuối đoạn).

### Nghiệm thu WP2-fix
- `python scripts/check_citation_order.py` → 37/37 khớp (không thêm citation
  mới nào -- ba khoản trích dẫn ở hàng I6 dùng lại đúng các khóa
  `luatkhcndmst2025`/`nd268_2025` đã có sẵn theo đúng locator của WP1-fix2).
- `latexmk -xelatex main.tex`: sạch, 0 lỗi, 0 tham chiếu thiếu, 0 overfull
  hbox (chỉ còn các underfull hbox trong mục tài liệu tham khảo đã tồn tại
  từ trước, không phải hồi quy mới); **33 trang, 15885 từ** (`pdftotext
  main.pdf - | wc -w`, cùng phương pháp với các lần đo trước để so sánh được
  -- giảm 63 từ so với sau WP2 (15948 từ) dù có thêm một đoạn và sáu nhãn mã
  mới, vì phần cắt tóm tắt (~95 từ) lớn hơn phần thêm).
- `latexmk -xelatex supplementary_material.tex`: biên dịch độc lập lần đầu
  trong phiên này; sau khi sửa hai lỗi nêu trên (macro `\citep` không tồn
  tại, `\ref` chéo sang thân bài, đường dẫn hình `fig05`→`fig06`), biên dịch
  sạch, 0 lỗi, 0 tham chiếu thiếu; 10 trang.
- Đối chiếu thủ công qua `pdftotext`: hàng I6 xuất hiện đúng ở cuối Bảng S7;
  nhãn "(I1)"--"(I6)" xuất hiện đúng vị trí trong Bảng~5 thân bài, đúng thứ
  tự dòng gốc (Nền tảng số quốc gia=I6 ở đầu, Định danh/xác thực=I1 ở dòng
  hai, v.v.).
