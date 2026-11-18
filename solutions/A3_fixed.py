# A3_fixed.py - solution to exercise A3, Topic A
# What it does: the corrected version of exercises/A3_find_the_bug.py - sorts the 10
#   timings before picking the p95 index, then prints the list and the p95.
# Concepts: the fix is the one line times.sort() before the index. Print the list next to
#   the percentile so the reader can check the figure themselves.
# How to run: python A3_fixed.py

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

repeats = 10

times = []

for i in range(repeats):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        times.append(response.json()["latency_ms"])

times.sort()
p95 = times[int(len(times) * 0.95) - 1]
print("Times:", times)
print("p95:", p95)
