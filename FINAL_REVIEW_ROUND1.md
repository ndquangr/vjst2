# FINAL REVIEW — Round 1 (10/08/2026)

## Kết luận tạm thời

Bản WP9.6 đã đạt mức ổn định cao về logic kiến trúc, truy vết, ranh giới với nghiên cứu trước và tính tái lập. Tuy nhiên **chưa nên nộp nguyên trạng**. Rủi ro lớn nhất hiện nay không phải thiếu đóng góp mà là bản thảo đang mang hình thức gần với một technical report: 41 trang A4, nhiều bảng truy vết có mật độ chữ rất cao, và chi tiết phương pháp/tái lập lấn át câu chuyện khoa học chính.

## P0 — phải xử lý trước khi nộp

1. **Độ dài và mật độ quá cao.** Bản QA hiện 41 trang (36 trang trước phần tài liệu tham khảo + 5 trang tài liệu tham khảo). Cần nén mạnh thân bài; mục tiêu thực dụng nên gần quy mô bản biên tập VJST trước (~25–30 trang theo layout tương đương), không giữ toàn bộ chi tiết traceability trong thân bài.
2. **Tách reproducibility package khỏi thân bài.** Các nội dung atomization rules, ví dụ truy vết một–nhiều/truy vết đầy đủ, chi tiết R1–R5, danh sách artefact và nhiều locator nguồn nên chuyển sang supplementary material. Thân bài chỉ giữ đủ để chứng minh phương pháp có thể tái lập.
3. **Giảm bảng quá dày.** Bảng 2–6 hiện có nhiều ô font rất nhỏ. Nên giữ ma trận/điểm quyết định ở mức tổng hợp, chuyển locator điều-khoản chi tiết sang supplement.
4. **Làm rõ bản chất đánh giá.** Abstract và phần kết luận cần nói rõ đây là *scenario-based architecture verification/stress-test*, không phải empirical validation, pilot deployment hay independent expert validation. Phần giới hạn hiện đã nêu đúng, nhưng thông điệp này cần xuất hiện sớm hơn để tránh reviewer hiểu sai mức chứng cứ.

## P1 — nên sửa

5. **Reference [2]**: bài JSTPM đã có volume/issue/pages đúng (15(2), 45–68), nhưng tên tạp chí đang để tiếng Việt trong danh mục tham khảo tiếng Anh. Website chính thức của tạp chí dùng tên `JOURNAL OF SCIENCE AND TECHNOLOGY POLICY AND MANAGEMENT`; nên dùng tên này để nhất quán với quy tắc references tiếng Anh.
6. **Đóng góp mới cần nổi hơn artefact.** Cuối Introduction nên có 1 đoạn rất ngắn, tối đa 3 đóng góp: (i) SRA tỉnh–trung ương có traceability; (ii) data-authority + variation/conformance; (iii) scenario refinement B1₀→B1-R/P-DIST. Các mã A1–A4/DRV/AD/AE/CR nên được coi là cơ chế chứng minh, không phải headline contribution.
7. **P-DIST**: luôn gọi rõ là profile triển khai *được đề xuất trong nghiên cứu*, tránh bất kỳ câu nào có thể khiến người đọc tưởng đây là một profile chính thức của C4.
8. **Front matter**: ở build QA 13 pt, tóm tắt tiếng Việt tràn sang trang 2 và bản tiếng Anh bắt đầu trang 3. Khi làm DOCX 12 pt/TNR cần kiểm tra lại để front matter gọn hơn và không tạo cảm giác bài bị kéo dài ngay từ đầu.

## P2 — tinh chỉnh trình bày

9. Các URL dài trong references tạo nhiều underfull boxes; chấp nhận được ở QA nhưng nên kiểm tra lại trong DOCX.
10. Các hình H1–H5 đọc được ở PDF hiện tại, nhưng chữ trong H1/H4/H5 sát ngưỡng nhỏ. Khi chuyển sang DOCX nên xuất hình vector/PDF hoặc SVG/EMF thay vì raster.
11. Build XeLaTeX hiện không có overfull box/citation/cross-reference undefined; chỉ còn font warnings và nhiều underfull boxes chủ yếu do bảng/reference. Đây là vấn đề typography, không phải lỗi logic.

## Đánh giá rủi ro reject hiện tại

- **Novelty/đóng góp**: thấp–trung bình sau WP9; ranh giới với nghiên cứu trước đã rõ.
- **Phương pháp**: trung bình; DSR + traceability khá chặt, nhưng reviewer có thể phản ứng nếu hiểu stress-test là validation thực nghiệm.
- **Evaluation**: trung bình; phù hợp với conceptual/design paper nếu claim được giới hạn đúng.
- **Trình bày/độ dài**: cao nhất hiện tại.
- **Tính tái lập**: mạnh; cần chuyển chi tiết sang supplementary package thay vì để trong thân bài.

## Figure reproducibility package

Đã tạo thư mục `figure_sources/` trong `Sources`, gồm 5 file TikZ/LaTeX độc lập, `build_figures.sh`, README hướng dẫn và PDF preview. Các file được trích trực tiếp từ các figure block hiện có trong `05_architecture.tex`, `06_data.tex`, `07_interop.tex`; không vẽ lại bằng suy đoán.

## Bước tiếp theo đề xuất

Final Review Round 2 nên thực hiện theo hướng **compression without loss of evidence**: xác định đoạn/bảng nào chuyển supplement, ước lượng số trang giảm được, rồi sửa thân bài theo từng nhóm P0 trước khi tạo DOCX nộp chính thức.
