WP3: chấm đường cơ sở B0 bằng cùng rubric và bổ sung vào bảng kết quả.
Note: sau WP1 và WP2 Bảng 5 đã thành Bảng 6 (tab:evaluation). Khi chạy WP3, thay mọi chỗ "Bảng 5" bằng tab:evaluation (dùng nhãn thay vì số, an toàn hơn).

Vấn đề: Mục 3.4 và 7.1 giới thiệu B0 (cấu hình tập trung) như đường cơ sở đối
chiếu. Bảng 5 KHÔNG có cột B0. Nhưng Mục 7.3 vẫn đưa nhận định về B0. Phản biện
sẽ đọc ra: tuyên bố có baseline, không có dữ liệu, vẫn kết luận về nó.

Việc cần làm:
1. Chấm B0 với cả 10 kịch bản SC1–SC10 bằng đúng rubric ba mức hiện có. Ghi kết
   quả vào một CSV mới evaluation_results_b0.csv theo đúng schema của
   evaluation_results.csv.
2. Chấm phải có lập luận, không tùy tiện. Với mỗi kịch bản, ghi neo kiến trúc và
   lý do xếp mức. Lưu ý B0 là tập trung nên các kịch bản về chuyển quyền ghi
   (SC9), tương thích phiên bản lệch thời điểm (SC10), gián đoạn lớp trung ương
   (SC4, SC7) sẽ cho profile rủi ro/đánh đổi KHÁC chứ không đơn giản là tốt hơn
   hoặc xấu hơn. Không được để kết quả nghiêng có lợi cho P-DIST.
3. 08_evaluation.tex: Bảng 5 thành bốn cột kết quả — B0 | B1 | B1-R | Hàm ý kiến
   trúc chính.
4. Viết lại Mục 7.3 dựa trên dữ liệu B0 thật thay vì nhận định chung. Giữ nguyên
   và nhấn mạnh cảnh báo: B0 và B1 khác nhau đồng thời ở nhiều quyết định nên
   không cho phép suy luận nhân quả về một quyết định riêng lẻ; đây là đối chiếu
   đánh đổi định tính, không phải xếp hạng.
5. Cập nhật supplementary_material.tex mục S12 cho khớp.

Nếu trong quá trình chấm phát hiện B0 làm lộ một khoảng trống mà B1-R chưa xử lý,
BÁO CÁO NGAY và dừng lại, đừng tự sửa kiến trúc.