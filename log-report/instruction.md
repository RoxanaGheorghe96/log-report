An Apache-style access log is at /app/access.log. Each line has the form:

<client_ip> - - [<timestamp>] "<METHOD> <path> HTTP/1.1" <status> <bytes>

Analyze the log and write a JSON object to /app/report.json with exactly these three keys:

1. "total_requests" — integer, the number of non-empty lines in the log.
2. "unique_ips" — integer, the number of distinct client IP addresses (the first whitespace-separated field of each line).
3. "top_path" — string, the request path that appears most often in the quoted request lines (in this log the most frequent path is strictly more frequent than any other, so no tie-breaking is needed).

Do not modify /app/access.log. The report must be valid JSON parseable by Python's json module.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
