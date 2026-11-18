# 04_sequential_vs_parallel.py - Topic B (concurrency), handout 02
# What it does: sends 10 requests one after another, times it, then sends the same 10
#   through a 5-worker thread pool and times that. Prints both totals in seconds.
# Concepts: throughput versus latency. Parallel work does not make a single answer
#   faster, it makes the batch finish sooner. ThreadPoolExecutor suits this because the
#   program is waiting on the network, not computing. Uses wall-clock time here, not
#   latency_ms, because the batch duration is what matters.
# How to run: python 04_sequential_vs_parallel.py
#   Uses the shared model quota - keep requests_count and workers as they are.

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

requests_count = 10
workers = 5


def ask_once(number):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    return requests.post(url, headers=headers, json=body)


start = time.time()
for number in range(requests_count):
    ask_once(number)
sequential_seconds = time.time() - start

start = time.time()
with ThreadPoolExecutor(max_workers=workers) as pool:
    results = list(pool.map(ask_once, range(requests_count)))
parallel_seconds = time.time() - start

print("One after another:", round(sequential_seconds, 1), "seconds")
print("With", workers, "at a time:", round(parallel_seconds, 1), "seconds")
