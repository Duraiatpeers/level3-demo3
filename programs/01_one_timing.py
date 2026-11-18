# 01_one_timing.py - Topic A (latency and percentiles), handout 01
# What it does: sends one question and prints the status code and the latency_ms value
#   the app returns with the answer.
# Concepts: the baseline call for this module. latency_ms is measured by the app itself,
#   so it covers retrieval plus the model, not your network wait. One timing tells you
#   almost nothing - that is the point of 02. Also the program to run first when
#   everything else says "No answer returned", because it prints the real status.
# How to run: app running on http://localhost:8000, environment variables set (handout 00),
#   then  python 01_one_timing.py

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}

response = requests.post(url, headers=headers, json=body)

print("Status:", response.status_code)
if response.status_code == 200:
    print("Latency in milliseconds:", response.json()["latency_ms"])
else:
    print("Body:", response.text)
