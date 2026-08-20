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