WP0: sửa các lỗi vệ sinh bản thảo. Chỉ sửa, không viết mới.

1. Tìm và xóa nhãn nội bộ còn sót ở đầu bản thảo/pipeline xuất docx:
   chuỗi "VJST2 - Round 3 strengthened SRA manuscript". Nó đang xuất hiện ở dòng
   đầu file docx được sinh ra. Tìm nguồn gốc (có thể trong main.tex,
   00_frontmatter.tex, hoặc script build docx) và loại bỏ.

2. Thống nhất tên phiên bản kiến trúc. Hiện đang lẫn lộn: "B10" (mục 3.4, 7.1,
   cột bảng 5), "B1" (tiêu đề Bảng 5), "B1-R" (bản tinh chỉnh), "b1r" (tên file
   CSV). Chọn MỘT bộ tên nhất quán: B1 cho ứng viên ban đầu, B1-R cho bản tinh
   chỉnh, B0 cho đường cơ sở tập trung. Áp dụng đồng bộ trong: tất cả file .tex,
   supplementary_material.tex, và tên/nội dung các file CSV
   (evaluation_results.csv, evaluation_results_b1r.csv,
   architecture_refinement_log.csv). Đổi tên file CSV nếu cần cho khớp.

3. Sửa trùng ký hiệu: các kịch bản đánh giá hiện là S1–S10, nhưng các mục của
   tài liệu bổ trợ cũng là S1–S12, gây trùng (ví dụ "S1" vừa là "Tập nguồn" vừa
   là "Tỉnh xử lý và quyết định"). Đổi kịch bản thành SC1–SC10 ở mọi nơi: thân
   bài, Bảng 5, tài liệu bổ trợ (S5, S12), và các CSV (evaluation_scenarios.csv,
   evaluation_results*.csv, scenario_coverage.csv).

4. Trong supplementary_material.tex mục S6, xóa câu placeholder chưa xử lý:
   "Trước khi nộp chính thức, gói dữ liệu bổ trợ nên được đóng băng thành một
   bản phát hành chỉ đọc và gắn định danh phiên bản/checksum. Các định danh phát
   hành được điền sau khi chốt bản nộp cuối..." — thay bằng chỗ trống chờ WP6
   điền DOI thật, đánh dấu bằng comment LaTeX % TODO-WP6.

5. deployment_view.csv đang rỗng (1 byte). Hoặc điền nội dung góc nhìn triển khai
   tương ứng Hình P-DIST trong supplement, hoặc xóa file và gỡ mọi tham chiếu tới
   nó. Báo cáo lựa chọn.

6. Bổ sung Luật Khoa học, Công nghệ và Đổi mới sáng tạo số 93/2025/QH15 vào
   refs.bib và references.tex. Tài liệu bổ trợ đã viện dẫn "Luật 93, khoản 3 Điều
   20" nhưng thân bài không có mục tham khảo tương ứng. NĐ 268 là văn bản hướng
   dẫn của chính luật này. Thêm trích dẫn ở Mục 1 nơi lần đầu nhắc NĐ 268, và
   đánh số lại toàn bộ danh mục nếu cần.

Nghiệm thu: compile sạch; grep toàn repo không còn "B10", không còn "Round 3";
mọi tham chiếu kịch bản đều dạng SC*; Luật 93/2025 có trong danh mục.