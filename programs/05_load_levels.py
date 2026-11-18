# 05_load_levels.py - Topic B, handout 02
# What it does: sends 20 requests at 1, 5 and 10 workers, and prints total seconds, p50,
#   p95 and errors for each level.
# Concepts: the load curve. As workers go up the batch finishes sooner, but per-request
#   p95 usually rises - queueing. Reporting both columns together is how you find the
#   level where the app is still acceptable. Builds on 02 (percentiles) and 04 (pools).
# How to run: python 05_load_levels.py
#   Uses the shared model quota - ask your trainer before raising the worker levels.

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

import time
from concurrent.futures import ThreadPoolExecutor

requests_count = 20


def ask_once(number):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    return requests.post(url, headers=headers, json=body)


for workers in [1, 5, 10]:
    start = time.time()
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(ask_once, range(requests_count)))
    seconds = time.time() - start

    times = []
    errors = 0
    for response in results:
        if response.status_code == 200:
            times.append(response.json()["latency_ms"])
        else:
            errors = errors + 1

    times.sort()
    if len(times) > 0:
        p50 = times[len(times) // 2]
        p95 = times[int(len(times) * 0.95) - 1]
    else:
        p50 = 0
        p95 = 0
    print("Workers:", workers, "| total seconds:", round(seconds, 1), "| p50:", p50, "| p95:", p95, "| errors:", errors)
