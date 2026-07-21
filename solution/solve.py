import json
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")

total_requests = 0
unique_ips = set()
path_counts = Counter()

for raw_line in LOG_PATH.read_text(encoding="utf-8").splitlines():
    line = raw_line.strip()
    if not line:
        continue

    total_requests += 1
    unique_ips.add(line.split()[0])
    request = line.split('"')[1].split()
    path_counts[request[1]] += 1

report = {
    "total_requests": total_requests,
    "unique_ips": len(unique_ips),
    "top_path": path_counts.most_common(1)[0][0],
}

REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
