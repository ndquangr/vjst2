Trước khi bắt đầu WP2, xử lý ba tồn đọng từ review WP1-fix (gộp chung commit,
ghi riêng trong REVISION_LOG):

a. 03_background.tex §2.3 đoạn 2, câu cuối bị vỡ ngữ pháp sau khi viết lại: mệnh
   đề "-- nghiệp vụ công nhận/chứng nhận DN KH&CN và DN KNST mà chưa hệ thống nào
   khác đảm nhiệm đầy đủ" không còn chủ ngữ để gắn vào. Tách thành câu độc lập
   phát biểu rõ: nghiệp vụ công nhận/chứng nhận DN KH&CN và DN KNST là phần chưa
   hệ thống hiện hữu nào đảm nhiệm đầy đủ, và đó là lý do tồn tại của nền tảng
   đề xuất.

b. Trong bảng tab:existing-systems, cụm "UBND cấp tỉnh (SoR nghiệp vụ)" lẫn chủ
   thể pháp lý với vai trò hệ thống. Theo định nghĩa của bài, SoR là vai trò của
   nút tỉnh đang giữ gán quyền ghi hiệu lực, không phải của cơ quan. Viết lại
   theo hướng: UBND cấp tỉnh là cơ quan mang nghĩa vụ; nút tỉnh trong kiến trúc
   là SoR nghiệp vụ. Grep toàn bài xem còn chỗ nào gán vai trò hệ thống cho cơ
   quan hoặc ngược lại.

c. Trong 07_interop.tex, dòng bảng "Nền tảng số quốc gia" hiện dài gấp ~3 lần các
   dòng khác và phần (b) về khoản 2 Điều 66 trùng với Mục 6.2 (subsec:sla) vốn
   xử lý kỹ hơn. Giữ (a) đầy đủ trong ô; rút (b) còn một câu ngắn kèm tham chiếu
   chéo tới Mục 6.2. Mục tiêu: độ dài ô tương đương các dòng còn lại.

Bổ sung vào nghiệm thu WP2 (ngoài các mục đã nêu trong prompt WP2):

d. Chạy scripts/check_citation_order.py, phải báo đủ số/số khớp.

e. Sau khi thêm hình máy trạng thái chuyển giao quyền ghi, kiểm tra lại toàn bộ
   đánh số hình và bảng: WP1 đã chèn Bảng 2 mới làm các bảng sau dịch lên một số.
   Xác nhận mọi \ref hình/bảng trong cả thân bài lẫn tài liệu bổ trợ đều trỏ đúng,
   và không còn tham chiếu cứng dạng "Hình 3"/"Bảng 5" viết tay.

f. Khi mở rộng Mục 5.2, phải nhất quán với phát biểu SoR mới ở §2.3: nút tỉnh
   đang giữ gán quyền ghi hiệu lực là SoR; lớp trung ương và Nền tảng số quốc gia
   chỉ giữ mô hình đọc/tổng hợp. Thêm một tham chiếu chéo hai chiều giữa §2.3 và
   Mục 5.2 để người đọc thấy đây là cùng một bất biến.

g. Báo cáo số trang và số từ trước/sau WP2, kèm mức tăng lũy kế so với trước WP1.