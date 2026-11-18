# 10_cost_regression_test.py - Topic E, handout 04
# What it does: two pytest tests that guard the budgets at the top of the file - average
#   tokens over 5 calls must stay under token_budget, and p95 over 10 calls must stay
#   under latency_budget_ms.
# Concepts: cost and speed as regression tests, so a prompt change that doubles the token
#   count fails in CI instead of surfacing on the bill. Budgets are a business decision,
#   not a measurement - set them from your own baseline (exercise E4). pytest.skip is
#   used when nothing came back, so an app that is down reads as "not tested", not "pass".
# How to run: python -m pytest 10_cost_regression_test.py -v

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

import pytest

token_budget = 2000
latency_budget_ms = 15000


def test_tokens_stay_within_budget():
    total = 0
    count = 0
    for i in range(5):
        body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            usage = response.json()["usage"]
            total = total + usage["prompt_tokens"] + usage["completion_tokens"]
            count = count + 1
    if count == 0:
        pytest.skip("no answers returned, nothing was tested")
    assert total / count <= token_budget


def test_p95_latency_stays_within_budget():
    times = []
    for i in range(10):
        body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            times.append(response.json()["latency_ms"])
    if len(times) == 0:
        pytest.skip("no answers returned, nothing was tested")
    times.sort()
    p95 = times[int(len(times) * 0.95) - 1]
    assert p95 <= latency_budget_ms
