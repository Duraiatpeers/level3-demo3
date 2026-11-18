# 06_find_throttling.py - Topic C (throttling), handout 02
# What it does: sends 30 requests at 5, 10 and 20 workers and counts ok, throttled and
#   other errors at each level. Throttling is spotted by "429" or "RateLimit" in the
#   response text.
# Concepts: a rate limit is a different failure from being slow - the request does not
#   arrive late, it does not arrive at all. The app returns the model's throttle as its
#   own error, so the marker is looked for in the body text, not only in status_code.
#   Finding the level where throttling starts is the deliverable (exercise C1).
# How to run: python 06_find_throttling.py
#   This is the heaviest program in the module and uses the shared quota - ask your
#   trainer before running it, and do not raise requests_count or the worker levels.

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

from concurrent.futures import ThreadPoolExecutor

requests_count = 30


def ask_once(number):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    return requests.post(url, headers=headers, json=body)


for workers in [5, 10, 20]:
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(ask_once, range(requests_count)))

    ok = 0
    throttled = 0
    other_errors = 0
    for response in results:
        if response.status_code == 200:
            ok = ok + 1
        elif "429" in response.text or "RateLimit" in response.text:
            throttled = throttled + 1
        else:
            other_errors = other_errors + 1
    print("Workers:", workers, "| ok:", ok, "| throttled:", throttled, "| other errors:", other_errors)
