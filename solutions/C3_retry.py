# C3_retry.py - solution to exercise C3, Topic C
# What it does: sends one request and, if the reply text contains 429, waits 2 seconds and
#   tries again, up to 3 tries. Prints the number of tries and the final status.
# Concepts: handling a rate limit instead of failing on it. Only throttling is retried -
#   any other error stops at once, because retrying a genuine failure just wastes quota.
#   The fixed 2-second wait is the simple version; production code backs off for longer
#   each time and caps the total wait, which is worth mentioning when you teach this.
# How to run: python C3_retry.py
#   Easiest to see while 06_find_throttling.py is producing throttles.

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

body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}

tries = 0
done = False

while tries < 3 and not done:
    tries = tries + 1
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        done = True
    elif "429" in response.text:
        time.sleep(2)
    else:
        done = True

print("Tries:", tries)
print("Status:", response.status_code)
