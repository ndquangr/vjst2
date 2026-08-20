WP1-fix: sửa lỗi phát hiện khi review WP1. Chạy trước khi bắt đầu WP bất kỳ khác.
Commit riêng, message "WP1-fix: sửa mâu thuẫn SoR, phạm vi căn cứ pháp lý và thứ
tự tài liệu tham khảo". Cập nhật REVISION_LOG.md.

1. [Chặn] Mâu thuẫn SoR. Trong 03_background.tex §2.3, câu "nền tảng đề xuất giữ
   vai trò hệ thống lưu bản ghi nghiệp vụ chính (SoR) cho nghiệp vụ công nhận/
   chứng nhận" và ô bảng "Nền tảng đề xuất là nguồn ghi cấp Bộ" mâu thuẫn với
   AD01 và bảng thẩm quyền dữ liệu ở 06_data.tex, nơi SoR nghiệp vụ là NÚT TỈNH
   đang có gán quyền ghi hiệu lực, còn trung ương chỉ giữ mô hình đọc/tổng hợp.
   Đọc lại 06_data.tex §5.1-5.2 và 05_architecture.tex AD01 trước khi sửa, rồi
   viết lại cho nhất quán: nền tảng là kiến trúc chuyên ngành trong đó các nút
   tỉnh giữ vai trò SoR cho trạng thái thuộc phạm vi thẩm quyền của mình; nền
   tảng KHÔNG phải "nguồn ghi cấp Bộ". Grep toàn repo cụm "nguồn ghi cấp Bộ" và
   "SoR" để đảm bảo không còn chỗ nào phát biểu ngược.

2. [Chặn] Nới phạm vi căn cứ pháp lý. Trong 07_interop.tex, dòng bảng mới về Nền
   tảng số quốc gia đang gộp hai nghĩa vụ khác nhau thành một. Sự thật trong văn
   bản: (a) NĐ 268 khoản 3 Điều 48 — UBND cấp tỉnh ĐỊNH KỲ cập nhật dữ liệu vòng
   đời GIẤY CHỨNG NHẬN DN KH&CN lên Nền tảng số quản lý KH,CN&ĐMST quốc gia; (b)
   NĐ 268 khoản 2 Điều 66 — UBND cấp tỉnh THÔNG BÁO cho Bộ KH&CN TRONG 15 NGÀY
   kể từ ngày ra quyết định, áp dụng cho cả các Giấy công nhận (gồm DN KNST) và
   Giấy chứng nhận DN KH&CN. Đây là hai cơ chế khác nhau về đối tượng nhận, phạm
   vi và nhịp thời gian. Tách thành hai phát biểu riêng trong ô bảng, mỗi phát
   biểu gắn đúng locator. Không được để một câu duy nhất ngụ ý DN KNST cũng có
   nghĩa vụ định kỳ cập nhật nền tảng quốc gia — văn bản không quy định như vậy.

3. [Chặn] Nghĩa vụ pháp lý gán cho phần mềm. Trong 03_background.tex §2.3 và ô
   bảng tương ứng, cụm "nền tảng đề xuất ... có nghĩa vụ cập nhật định kỳ lên
   nền tảng quốc gia" gán một nghĩa vụ L1 cho một hệ thống phần mềm. Nghĩa vụ
   thuộc về UBND cấp tỉnh. Viết lại theo hướng: nền tảng là phương tiện kỹ thuật
   hỗ trợ cơ quan có thẩm quyền thực hiện nghĩa vụ đó. Rà cả bài xem còn chỗ nào
   gán nghĩa vụ pháp lý cho nền tảng/hệ thống thay vì cho chủ thể.

4. [Chặn] Thứ tự references.tex. Đối chiếu tự động cho thấy 35/37 mục khớp thứ
   tự trích dẫn lần đầu, riêng vị trí 28-29 bị đảo: luatdulieu2024 được trích lần
   đầu TRƯỚC qd1762_2025 (cùng đoạn cuối §2.3). Đổi lại thứ tự hai bibitem này.
   Sau đó viết một script kiểm tra thứ tự (quét \cite* theo đúng thứ tự \input
   trong main.tex, so với thứ tự \bibitem) và lưu vào repo để dùng lại ở các WP
   sau; chạy nó như bước nghiệm thu bắt buộc mỗi WP.

5. Locator đảo chiều: câu liệt kê "CSDL Nhiệm vụ khoa học và công nghệ và CSDL
   Doanh nghiệp khởi nghiệp" nhưng locator ghi "Phụ lục, STT 38, 43". Thực tế
   STT 38 = CSDL Doanh nghiệp khởi nghiệp, STT 43 = CSDL Nhiệm vụ khoa học và
   công nghệ. Sửa cho khớp thứ tự.

6. Bỏ phụ thuộc vào nguồn không trích dẫn được cho hệ thống quản lý nhiệm vụ.
   Đổi tên dòng bảng và cách gọi trong prose thành "Hệ thống quản lý nhiệm vụ
   KH&CN trực tuyến của Bộ", neo bằng HAI căn cứ có văn bản: nhóm dữ liệu giao
   dịch KH&CN theo QĐ 1973, và QĐ 1762 Phụ lục STT 43 "CSDL Nhiệm vụ khoa học và
   công nghệ" (đơn vị chủ trì: Cục Thông tin, Thống kê). Với hai căn cứ này, lập
   luận "không thiết kế lại quy trình quản lý nhiệm vụ KH&CN" đứng vững bằng văn
   bản và có thể BỎ nhãn \textsc{cần bổ sung}. Nếu vẫn muốn nhắc tên miền
   stm.mst.gov.vn, để trong ngoặc như ví dụ vận hành, không làm căn cứ.

7. Bổ sung lập luận đang bỏ lỡ. Điểm chẩn đoán C07 trong tài liệu bổ trợ (mục
   S10.3 và S11) đã ghi nhận rằng phạm vi CSDL trong QĐ 1762 chưa trùng với hai
   miền DN KH&CN/DN KNST. §2.3 là chỗ đúng để nêu: danh mục QĐ 1762 đăng ký CSDL
   Doanh nghiệp khởi nghiệp (STT 38) nhưng không có mục tương ứng cho DN KH&CN.
   Thêm 1-2 câu, tham chiếu chéo tới mục chẩn đoán trong tài liệu bổ trợ, và giữ
   nguyên trạng thái "cần làm rõ" — KHÔNG nâng thành xung đột hay dùng để khóa
   thiết kế. Điều này củng cố lập luận khoảng trống bằng bằng chứng văn bản.

8. Bibitem luatkhcndmst2025 thiếu URL và ngày truy cập trong khi mọi mục văn bản
   pháp luật khác đều có. Bổ sung nếu tìm được nguồn công khai; nếu không, giữ
   định dạng nhất quán với các mục không có URL và báo lại cho tôi.

9. Revert phần nén Mục 8.2 trong 09_discussion.tex. Khôi phục P1/P2/P3 thành ba
   đoạn riêng có nhãn đậm như bản trước WP1. Lý do: ba nguyên tắc này chính là
   phần design knowledge có khả năng khái quát — tức đóng góp khoa học mà WP2 sẽ
   làm nổi bật; nén chúng làm yếu đúng thứ cần mạnh. Giữ lại một câu ngắn trỏ
   ngược về Mục 4.1-4.3 để tránh lặp lập luận nền.
   Bù ngân sách độ dài ở hai chỗ khác: (a) trong Bảng 6 (conformance), gộp hai
   dòng khung kiến trúc QĐ 3090 và QĐ 292 thành một dòng vì cùng một loại lập
   luận; (b) trong 07_interop.tex §6.4, đoạn mô tả P-DIST lặp lại nội dung đã có
   ở §4.3 và §5.1 — rút gọn còn phần thực sự mới của mục này. Báo cáo số từ
   trước/sau cho từng chỗ.

Nghiệm thu: script kiểm tra thứ tự trích dẫn báo 37/37 khớp; grep không còn
"nguồn ghi cấp Bộ"; mọi phát biểu về SoR trong bài nhất quán với AD01; compile
sạch; báo cáo số từ và số trang.