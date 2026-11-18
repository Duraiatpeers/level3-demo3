# A3_find_the_bug.py - exercise A3, Topic A (see exercises_A_latency.md)
# What it does: meant to collect 10 timings and print p95. It runs and prints a number,
#   but the number is not the p95 - it changes meaninglessly from run to run.
# Concepts: a percentile is only a percentile if the list is in order. One step is missing
#   between collecting and indexing; compare the printed times with the printed p95 to see
#   it, then check solutions/A3_fixed.py.
# How to run: python A3_find_the_bug.py

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

p95 = times[int(len(times) * 0.95) - 1]
print("Times:", times)
print("p95:", p95)
