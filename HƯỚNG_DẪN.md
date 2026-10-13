# Hướng dẫn nộp bài

## 1. Cấu trúc bài nộp

Bài nộp là một tệp ZIP không quá 100 MB. Ví dụ đội `team001` nộp tệp `team001.zip` có cấu trúc:

```text
team001.zip
|-- Dockerfile
|-- run.sh
|-- main.py
`-- ...
```

`Dockerfile` và `run.sh` phải nằm ngay ở gốc tệp ZIP, không đặt trong một thư mục con khác.

Ảnh Docker phải chạy trên Linux `amd64`, không dùng GPU và chứa sẵn toàn bộ mã nguồn cùng thư viện cần thiết. Không đưa khóa API vào bài nộp.

## 2. Cách hệ thống khởi động bài làm

Ảnh Docker phải khai báo đúng dòng sau:

```dockerfile
ENTRYPOINT ["./run.sh"]
```

Sau khi dựng ảnh Docker, tệp `run.sh` phải có dòng đầu tiên là `#!/bin/sh`, có quyền thực thi và chuyển toàn bộ tham số nhận được sang chương trình chính bằng `"$@"`.

Ví dụ `run.sh` cho bài làm bằng Python:

```sh
#!/bin/sh
set -eu
exec python main.py "$@"
```

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

## 5. Chạy thử bằng Docker

Mở terminal tại thư mục bài làm, ví dụ `team001/`, rồi dựng ảnh:

```bash
docker build --platform linux/amd64 -t team001 .
```

Chạy thử với dữ liệu mẫu trên máy:

```bash
docker run --rm \
  --mount type=bind,src=<duong-dan-tuyet-doi>/xlsx_files,dst=/input/xlsx_files,readonly \
  --mount type=bind,src=<duong-dan-tuyet-doi>/queries.json,dst=/input/queries.json,readonly \
  --mount type=bind,src=<thu-muc-ket-qua-tuyet-doi>,dst=/output \
  team001 \
  --xlsx-dir /input/xlsx_files \
  --queries /input/queries.json \
  --output /output/submission.csv \
  --openrouter-key <key> \
  --openrouter-model qwen/qwen3.7-flash \
  --openrouter-base-url https://openrouter.ai/api/v1
```

Sau khi chạy xong, kiểm tra tệp `submission.csv` trong thư mục kết quả.

## 6. Giới hạn

- Nền tảng: Linux `amd64`, không GPU.
- Tối đa 6 CPU và 1 GB RAM cho mỗi lượt chạy.
- Tối đa 40 phút cho toàn bộ tập dữ liệu.
- Mô hình chính thức: `qwen/qwen3.7-flash` qua OpenRouter.
- Chi phí LLM tối đa: 0,10 USD nhân với số câu hỏi, tính cả các lần gọi lại.

## 7. Kiểm tra trước khi nộp

- `Dockerfile` và `run.sh` nằm ở gốc tệp ZIP.
- `ENTRYPOINT` là chính xác `["./run.sh"]`.
- Ảnh dựng được cho `linux/amd64` và không cần GPU.
- Chương trình nhận đủ sáu tham số và không sửa `/input`.
- `submission.csv` là UTF-8, có header `id,answer` và mỗi `id` xuất hiện đúng một lần.
- Bài nộp không chứa khóa API và không vượt quá 100 MB.
