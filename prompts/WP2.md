WP2: nâng mô hình quyền ghi theo phạm vi và thời gian thành đóng góp số 1 của bài.

Vấn đề: thứ duy nhất trong bài mang tính thiết kế mới và tổng quát hóa được ra
ngoài miền DN KH&CN — mô hình gán quyền ghi có write_scope + jurisdiction_id +
khoảng hiệu lực + writer_epoch đơn điệu + máy trạng thái chuyển giao
prepared → old-frozen → cutover-confirmed → new-active → completed, với bất biến
một writer hợp lệ — đang nằm trong tài liệu bổ trợ (S9.2, S10.1), còn thân bài chỉ
có một đoạn ngắn ở Mục 5.2. Đây là đóng góp mạnh nhất nhưng đang bị chôn.

Việc cần làm:

1. 06_data.tex, Mục 5.2: mở rộng từ một đoạn thành một tiểu mục hoàn chỉnh
   (400–500 từ). Đưa từ supplement lên: cấu trúc bản ghi gán quyền ghi (bốn nhóm
   trường), bất biến single-active-writer, chuỗi trạng thái chuyển giao, quy tắc
   hủy/phục hồi tiến, quy tắc xác minh epoch khi nút khởi động lại sau gián đoạn.
   Giữ mức L2: KHÔNG khóa thuật toán consensus, cơ chế khóa hay middleware.
   Nêu rõ tính tổng quát: mô hình này áp dụng được cho bất kỳ nền tảng chính phủ
   đa cấp nào có chuyển giao thẩm quyền theo thời gian, không riêng miền này.

2. Thêm một hình mới: máy trạng thái chuyển giao quyền ghi. Tạo file nguồn trong
   figure_sources/ theo đúng công cụ/định dạng của các hình hiện có (đọc các file
   nguồn hiện tại để theo đúng convention). Năm trạng thái, các chuyển tiếp, điều
   kiện, và điểm không thể hủy sau new-active. Chèn vào Mục 5.2, đánh số và cập
   nhật mọi tham chiếu chéo của các hình sau nó.

3. 01_abstract.tex: viết lại phần kết quả của cả bản tiếng Việt và tiếng Anh để
   đóng góp này xuất hiện bằng tên gọi cụ thể, thay vì chỉ nói chung "gắn quyền
   ghi với thẩm quyền và thời gian hiệu lực". Đồng thời BỎ ba con số 16/116/128
   khỏi tóm tắt — chúng đo công sức mã hóa chứ không phải phát hiện, và chính Mục
   3.2 đã thừa nhận 128 không phải số yêu cầu ngữ nghĩa sau khử trùng lặp. Giữ
   các con số này ở Mục 3.2. Thay chỗ trống bằng phát biểu về phát hiện.

4. 02_intro.tex: trong đoạn "Bài đóng góp ba kết quả chính", đảo thứ tự để mô hình
   quyền ghi theo thời gian là đóng góp thứ nhất, và phát biểu nó như một kết quả
   thiết kế có tên chứ không phải một chi tiết của mô hình dữ liệu.

5. 10_conclusion.tex: chỉnh câu tổng kết đóng góp cho khớp thứ tự mới.

6. supplementary_material.tex: giữ lại ở S9.2/S10.1 phần chi tiết trường dữ liệu
   và các quy tắc kiểm chứng, nhưng bỏ phần đã được nâng lên thân bài để tránh
   trùng lặp nguyên văn. Thêm dòng trỏ ngược về Mục 5.2.