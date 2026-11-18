# 03_slowest_question.py - Topic A, handout 01
# What it does: runs three different questions 5 times each and prints the average
#   latency per question - a simple fact lookup, a maintenance question, and a comparison
#   between two pumps.
# Concepts: latency depends on the question, not just the app. The comparison question
#   needs more retrieved text and a longer answer, so it costs more time. Profile by
#   question type before you blame the infrastructure.
# How to run: python 03_slowest_question.py

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

repeats = 5

questions = [
    "What is the maximum operating pressure of the PX-100?",
    "How often does the PX-200 need preventive maintenance?",
    "Which pump allows 15 bar, the PX-100 or the PX-200?",
]

for question in questions:
    total = 0
    count = 0
    for i in range(repeats):
        body = {"question": question, "prompt_version": "v1"}
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            total = total + response.json()["latency_ms"]
            count = count + 1
        else:
            print("Failed:", response.status_code, response.text[:200])
    if count > 0:
        print(question[:50], "| average ms:", total // count)
    else:
        print(question[:50], "| no answers returned")
