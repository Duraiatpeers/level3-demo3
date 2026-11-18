# 09_compare_versions.py - Topic E (cost without losing quality), handout 04
# What it does: runs the same five questions on prompt versions v1, v2 and v2_1, 3 times
#   each, and prints correct answers, average tokens and average ms per version.
# Concepts: never judge a cost saving without a quality column beside it. Quality here is
#   "does the expected word appear in the answer" - cheap, repeatable, and wrong in both
#   directions, which is worth saying out loud to learners. Decide your accept rule
#   before you read the table, e.g. "no fewer correct than v1".
#   Each check is [question, word that must appear]; add your own pairs for exercise E2.
# How to run: python 09_compare_versions.py
#   This sends 3 versions x 5 questions x repeats - raising repeats multiplies the run.

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

repeats = 3

checks = [
    ["What is the maximum operating pressure of the PX-100?", "10 bar"],
    ["How often does the PX-200 need preventive maintenance?", "3 months"],
    ["Lubricant replacement interval for the PX-100?", "12 months"],
    ["max flow rate px 200??", "80"],
    ["Which pump allows 15 bar, the PX-100 or the PX-200?", "PX-200"],
]

for version in ["v1", "v2", "v2_1"]:
    correct = 0
    answered = 0
    tokens = 0
    time_total = 0
    for check in checks:
        for i in range(repeats):
            body = {"question": check[0], "prompt_version": version}
            response = requests.post(url, headers=headers, json=body)
            if response.status_code == 200:
                data = response.json()
                answered = answered + 1
                tokens = tokens + data["usage"]["prompt_tokens"] + data["usage"]["completion_tokens"]
                time_total = time_total + data["latency_ms"]
                if check[1] in data["answer"]:
                    correct = correct + 1
    if answered > 0:
        print(version, "| correct:", correct, "of", answered, "| average tokens:", tokens // answered, "| average ms:", time_total // answered)
    else:
        print(version, "| no answers returned (is this prompt_version supported by the app?)")
