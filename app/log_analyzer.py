import re
from collections import defaultdict

FAILED_LOGIN_PATTERN = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

def analyze_logs(file_path):
    ip_attempts = defaultdict(int)

    with open(file_path, "r") as f:
        for line in f:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip = match.group(1)
                ip_attempts[ip] += 1

    suspicious_ips = []

    for ip, count in ip_attempts.items():
        if count > 5:  # threshold
            suspicious_ips.append({
                "ip": ip,
                "attempts": count,
                "status": "suspicious"
            })

    return suspicious_ips