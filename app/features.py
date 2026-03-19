import pandas as pd
from collections import defaultdict
from datetime import datetime
import re

FAILED_LOGIN_PATTERN = re.compile(r"Failed password.*from (\d+\.\d+\.\d+\.\d+)")

def extract_features(file_path):
    ip_attempts = defaultdict(list)

    with open(file_path, "r") as f:
        for line in f:
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip = match.group(1)
                # For simplicity, just using count per IP
                timestamp = datetime.now()  # you could parse real timestamps if present
                ip_attempts[ip].append(timestamp)

    # Convert to DataFrame
    data = []
    for ip, times in ip_attempts.items():
        data.append({
            "ip": ip,
            "count": len(times),
            "avg_time_diff": (sum([(times[i]-times[i-1]).total_seconds() 
                                   for i in range(1,len(times))])/len(times[1:])) if len(times)>1 else 0
        })

    df = pd.DataFrame(data)
    return df