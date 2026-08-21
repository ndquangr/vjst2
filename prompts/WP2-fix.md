WP2-fix: hai việc trước khi sang WP3. Commit riêng, ghi REVISION_LOG.

1. Ma trận liên thông bốn lớp EIF ở Mục S7 tài liệu bổ trợ hiện có I1--I5, nhưng
   Bảng 5 ở thân bài (tab:lienthong) đã có 6 ranh giới sau khi WP1 thêm dòng
   "Nền tảng số quốc gia". Ranh giới mới chưa được ánh xạ bốn lớp -- vi phạm
   chính phương pháp mà Mục 6 tuyên bố.

   Thêm một dòng cho ranh giới này vào ma trận S7, đủ bốn lớp:
   - Pháp lý: Luật 93/2025 khoản 3 Điều 20 (Nhà nước xây dựng, vận hành Nền tảng
     số quốc gia); NĐ 268 khoản 3 Điều 48 (UBND cấp tỉnh định kỳ cập nhật dữ liệu
     vòng đời Giấy chứng nhận DN KH&CN); NĐ 268 khoản 2 Điều 66 (thông báo Bộ
     trong 15 ngày, gồm cả Giấy công nhận DN KNST). Giữ đúng phạm vi từng khoản,
     không gộp -- đây là lỗi đã sửa ở WP1-fix, đừng tái tạo lại trong bổ trợ.
   - Tổ chức: nền tảng quốc gia tổng hợp/kết nối/quan sát liên ngành; UBND cấp
     tỉnh là chủ thể mang nghĩa vụ; nút tỉnh là SoR nghiệp vụ; nền tảng đề xuất
     là phương tiện kỹ thuật, không mang nghĩa vụ pháp lý.
   - Ngữ nghĩa: hợp đồng dữ liệu cho sự kiện cập nhật/thông báo phải giữ loại
     giấy (chứng nhận DN KH&CN vs công nhận DN KNST), cơ quan quyết định, ngày
     quyết định/hiệu lực, trạng thái vòng đời, nguồn và phiên bản; hai loại sự
     kiện mang định danh và đích nhận tách biệt.
   - Kỹ thuật: đi qua cổng tích hợp và hạ tầng chia sẻ/điều phối theo quy định;
     gửi lại phải lũy đẳng và giữ bằng chứng gửi--nhận; không mở nhánh báo cáo
     song song. Giao thức, chu kỳ, kiểu API vẫn là L3.

   Về đánh mã: dòng mới đứng ĐẦU Bảng 5 nên nếu gán I6 thì thứ tự mã lệch thứ tự
   bảng. Chọn một trong hai và làm nhất quán, báo lại lựa chọn:
   (a) chèn thành I1 và dời I1--I5 cũ thành I2--I6, cập nhật mọi tham chiếu
       "I<n>" trong repo (đáng chú ý viewpoint_registry.csv V6 đang trỏ "Bảng
       5/I1" -- nếu đổi số thì phải trỏ đúng dòng Định danh/xác thực, không phải
       dòng mới); hoặc
   (b) giữ I1--I5, thêm I6, và bổ sung cột/nhãn mã I<n> hiển thị ngay trong Bảng
       5 ở thân bài để người đọc thấy ánh xạ, chấp nhận thứ tự mã không trùng
       thứ tự dòng.
   Tôi nghiêng về (b) vì ít rủi ro lan tỏa hơn và làm ánh xạ thân bài--bổ trợ
   hiện rõ, nhưng CC cứ đánh giá lại và báo lý do.

2. Tóm tắt tiếng Việt hiện 324 từ, vượt khung 160--250 của tạp chí; bản tiếng
   Anh 201 từ. Rút bản Việt về khoảng 230--240 từ, và quan trọng hơn là làm hai
   bản TƯƠNG ĐƯƠNG về nội dung -- hiện bản Việt nói nhiều hơn bản Anh.
   Nguyên tắc cắt, theo thứ tự ưu tiên giữ lại: (i) bối cảnh bài toán 1 câu;
   (ii) phương pháp DSR + SRA có truy vết 1 câu; (iii) phát hiện trung tâm về gán
   quyền ghi và bất biến single-active-writer -- GIỮ NGUYÊN, đây là đóng góp số 1;
   (iv) kết quả mười kịch bản và hậu kiểm; (v) ba nguyên tắc thiết kế, có thể rút
   thành cụm ngắn thay vì liệt kê đầy đủ ba mệnh đề; (vi) câu giới hạn về
   scenario-based verification -- GIỮ NGUYÊN, không được làm nhẹ đi.
   Chỗ cắt được nhiều nhất là câu mô tả SRA tách lõi/điểm biến thiên (trùng ý với
   phần sau) và phần liệt kê ba nguyên tắc. Sau khi cắt, đếm lại cả hai bản và
   báo cáo số từ.

Nghiệm thu: chạy scripts/check_citation_order.py; biên dịch sạch cả main và
supplementary; báo số từ tóm tắt VN/EN và số trang.