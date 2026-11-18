# 02_ten_timings.py - Topic A, handout 01
# What it does: sends the same question 10 times, sorts the timings and prints average,
#   p50, p95, slowest and the error count.
# Concepts: percentiles, and why an average hides the problem - p95 is the slow tail your
#   users actually complain about. Note the sort before the percentile; without it the
#   index means nothing (that is exercise A3). With 10 timings p95 is the 9th value, so
#   it is a rough figure - say the sample size when you report it.
# How to run: python 02_ten_timings.py

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
errors = 0

for i in range(repeats):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        times.append(response.json()["latency_ms"])
    else:
        errors = errors + 1

times.sort()
print("Sorted times:", times)

if len(times) > 0:
    p50 = times[len(times) // 2]
    p95 = times[int(len(times) * 0.95) - 1]
    average = sum(times) // len(times)
    print("Average:", average)
    print("p50:", p50)
    print("p95:", p95)
    print("Slowest:", times[-1])
print("Errors:", errors)
