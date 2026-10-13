# Hướng dẫn nộp bài

## 1. Cấu trúc bài nộp

Bài nộp sử dụng Python và là một tệp ZIP không quá 100 MB. Ví dụ đội `team001` nộp tệp `team001.zip` có cấu trúc:

```text
team001.zip
|-- Dockerfile
|-- main.py
`-- ...
```

`Dockerfile` và `main.py` phải nằm ngay ở gốc tệp ZIP, không đặt trong một thư mục con khác.

Ảnh Docker phải chạy trên Linux `amd64`, không dùng GPU và chứa sẵn toàn bộ mã nguồn cùng thư viện cần thiết. Không đưa khóa API vào bài nộp.

## 2. Cách hệ thống khởi động bài làm

Ảnh Docker phải khai báo đúng dòng sau:

```dockerfile
ENTRYPOINT ["python", "main.py"]
```

Khi container khởi động, Docker chạy trực tiếp `main.py`. Tệp này phải nhận các tham số dòng lệnh do hệ thống chấm cung cấp và chỉ thoát với mã `0` sau khi đã ghi xong kết quả.

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
