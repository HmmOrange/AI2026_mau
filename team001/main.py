import argparse
import csv
import json
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("--xlsx-dir", type=Path, required=True)
parser.add_argument("--queries", type=Path, required=True)
parser.add_argument("--output", type=Path, default=Path("output/team001/submission.csv"))
parser.add_argument("--openrouter-key", required=True)
parser.add_argument("--openrouter-model", required=True)
parser.add_argument("--openrouter-base-url", required=True)
args = parser.parse_args()

data = json.loads(args.queries.read_text(encoding="utf-8-sig"))
queries = data["queries"] if isinstance(data, dict) else data

args.output.parent.mkdir(parents=True, exist_ok=True)
with args.output.open("w", encoding="utf-8", newline="") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(["id", "answer"])
    for query in queries:
        answer = "TODO"  # Thay bằng phần xử lý câu hỏi của đội.
        writer.writerow([query["id"], answer])
