# Figure source package

Bộ này chứa **mã TikZ độc lập** của 6 hình kiến trúc trong bản thảo VJST2. Mỗi tệp `.tex` lấy nguyên khối `tikzpicture` từ source bài báo tại thời điểm final review, sau đó bọc bằng một preamble tối thiểu để có thể biên dịch độc lập bằng XeLaTeX.

## Cách dùng

```bash
bash build_figures.sh
```

Hoặc:

```bash
xelatex -interaction=nonstopmode -halt-on-error fig01_archimate_context.tex
```

Nếu máy có Times New Roman thì script dùng Times New Roman; nếu không có sẽ tự rơi về DejaVu Serif để QA. Việc đổi màu, kích thước hộp, vị trí node, nhãn và đường nối thực hiện trực tiếp trong `tikzpicture`.

## Ánh xạ với bài báo

| Hình | Tệp | Ký pháp/góc nhìn | Source gốc |
|---|---|---|---|
| Hình 1 | `fig01_archimate_context.tex` | ArchiMate động lực--ứng dụng | `05_architecture.tex` |
| Hình 2 | `fig02_archimate_capability_application.tex` | ArchiMate năng lực--ứng dụng | `05_architecture.tex` |
| Hình 3 | `fig03_archimate_data_authority.tex` | ArchiMate ứng dụng--dữ liệu | `06_data.tex` |
| Hình 4 | `fig04_write_authority_transfer_fsm.tex` | UML State Machine -- chuyển giao quyền ghi (AD01) | `06_data.tex` |
| Hình 5 | `fig05_c4_container_boundaries.tex` | C4 Container | `07_interop.tex` |
| Hình 6 | `fig06_c4_deployment_pdist.tex` | C4 Deployment / P-DIST | `07_interop.tex` |

## Nguyên tắc khi chỉnh

- TikZ chỉ là công cụ vẽ; giữ nguyên ngữ nghĩa ArchiMate/C4/UML đã nêu trong caption và phần phương pháp.
- Nếu đổi tên một `Container`, `Application Component`, `Data Object`, `Deployment Node`, trạng thái UML hoặc loại quan hệ, phải đồng bộ với prose và các bảng/registry liên quan.
- Hình 4 biểu diễn máy trạng thái ở mức L2 (ngữ nghĩa trường/trạng thái); thuật toán khóa, consensus hay middleware cụ thể vẫn thuộc L3.
- Hình 6 là profile triển khai P-DIST, không phải topology bắt buộc của lõi SRA.
- Hình 1--3 dùng ngữ nghĩa ArchiMate; Hình 4 dùng UML State Machine; Hình 5--6 dùng C4. Không trộn thêm ký pháp khác trong cùng hình nếu không sửa lại legend/caption và lập luận phương pháp.
