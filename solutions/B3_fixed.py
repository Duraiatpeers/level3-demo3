# B3_fixed.py - solution to exercise B3, Topic B
# What it does: the corrected version of exercises/B3_find_the_bug.py - start the clock,
#   run the 10 requests through the pool, then stop the clock and print the total.
# Concepts: the elapsed time must be taken after the work, and after the "with" block has
#   closed, because that is where the pool waits for all workers to finish.
# How to run: python B3_fixed.py

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

with ThreadPoolExecutor(max_workers=workers) as pool:
    results = list(pool.map(ask_once, range(requests_count)))

seconds = time.time() - start

print("Total seconds:", round(seconds, 1))
