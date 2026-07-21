There is an Apache-style access log at /app/access.log. Read the log and create a traffic summary at the absolute path /app/report.json.

1. /app/report.json must exist and contain one valid JSON object with exactly these three keys: total_requests, unique_ips, and top_path.
2. total_requests must be an integer equal to the number of non-empty lines in /app/access.log, counting each non-empty line as one request.
3. unique_ips must be an integer equal to the number of distinct client IP addresses. The client IP address is the first field of each non-empty log line.
4. top_path must be a string containing the most frequently requested path. The path is the second component of the quoted HTTP request, such as /index.html in "GET /index.html HTTP/1.1".

Write the completed report only to /app/report.json.
