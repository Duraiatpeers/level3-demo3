# B3_find_the_bug.py - exercise B3, Topic B (see exercises_B_concurrency.md)
# What it does: meant to time 10 parallel requests, but always reports about 0.0 seconds.
# Concepts: where you take the second timestamp decides what you measured. Look at the
#   order of the three blocks - start, the work, and the subtraction - then compare with
#   solutions/B3_fixed.py. A timer that reports 0.0 is a reminder to sanity-check a
#   performance result against the clock on the wall.
# How to run: python B3_find_the_bug.py

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
seconds = time.time() - start

with ThreadPoolExecutor(max_workers=workers) as pool:
    results = list(pool.map(ask_once, range(requests_count)))

print("Total seconds:", round(seconds, 1))
