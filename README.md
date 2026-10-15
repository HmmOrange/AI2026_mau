# Hướng dẫn nộp bài

## 1. Cấu trúc bài nộp

Bài nộp là một tệp ZIP không quá 100 MB. Tên file zip đặt theo tên đội, ví dụ đội tên là team001 thì tên file là team001.zip. Chỉ `Dockerfile` bắt buộc phải nằm ngay ở thư mục gốc; tên và cấu trúc các tệp còn lại do đội tự chọn:

```text
team001.zip
|-- Dockerfile
`-- ...mã nguồn và tệp cần thiết...
```

`Dockerfile` phải nằm ngay ở gốc tệp ZIP, không đặt trong một thư mục con khác.

Ảnh Docker phải chạy trên Linux `amd64`, không dùng GPU và chứa sẵn toàn bộ mã nguồn cùng thư viện cần thiết. Không đưa khóa API vào bài nộp.

## 2. Entrypoint

Ảnh Docker phải khai báo `ENTRYPOINT` để nhận các tham số dòng lệnh từ hệ thống chấm. Không bắt buộc ngôn ngữ hoặc tên tệp cụ thể.

Python:

```dockerfile
ENTRYPOINT ["python", "main.py"]
```

JavaScript:

```dockerfile
ENTRYPOINT ["node", "main.js"]
```

Rust:

```dockerfile
ENTRYPOINT ["./app"]
```

Chương trình được khai báo trong `ENTRYPOINT` phải nhận các tham số do hệ thống chấm cung cấp và chỉ thoát với mã `0` sau khi đã ghi xong kết quả.

## 3. Các tham số hệ thống cung cấp

Hệ thống chạy bài làm với sáu tham số:

```text
--xlsx-dir /input/xlsx_files
--queries /input/queries.json
--output /output/submission.csv
--openrouter-key <key>
--openrouter-model qwen/qwen3.7-flash
--openrouter-base-url https://openrouter.ai/api/v1
```

Chương trình phải:

- đọc các bảng tính trong thư mục nhận từ `--xlsx-dir`;
- đọc danh sách câu hỏi từ tệp nhận từ `--queries`;
- ghi kết quả vào đúng đường dẫn nhận từ `--output`;
- không sửa dữ liệu trong `/input`;
- ghi nhật ký ra stdout hoặc stderr, không ghi lẫn vào tệp kết quả.

## 4. Định dạng kết quả

Tệp kết quả phải là CSV UTF-8 với đúng hai cột `id,answer`:

```csv
id,answer
1,11
2,Ngo
```

Mỗi `id` trong `queries.json` phải xuất hiện đúng một lần. Không được thiếu, trùng hoặc thêm `id`. Cột `answer` chỉ chứa đáp án cuối cùng, không kèm giải thích.
