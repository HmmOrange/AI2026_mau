# Mẫu bài thi AI 2026

Repo này chứa hướng dẫn và một bài nộp mẫu tối giản trong thư mục `team001/`.

## Bắt đầu nhanh

1. Đổi tên thư mục `team001` thành tên đội.
2. Viết phần xử lý câu hỏi trong `main.py`.
3. Dựng và chạy thử bằng Docker theo [HƯỚNG_DẪN.md](HƯỚNG_DẪN.md).
4. Nén nội dung thư mục đội thành tệp ZIP để nộp. `Dockerfile` và `run.sh` phải nằm ngay ở gốc tệp ZIP.

Không đưa khóa OpenRouter vào mã nguồn hoặc tệp ZIP.

Có thể chạy nhanh bộ khung mà chưa cần Docker:

```bash
python team001/main.py --xlsx-dir sample-data/xlsx_files --queries sample-data/queries.json --openrouter-key test --openrouter-model qwen/qwen3.7-flash --openrouter-base-url https://openrouter.ai/api/v1
```

Lệnh này tạo `output/team001/submission.csv` với đáp án mẫu `TODO`.
