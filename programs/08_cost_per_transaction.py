# 08_cost_per_transaction.py - Topic D, handout 03
# What it does: runs the same question 10 times, averages the tokens in and out, applies
#   the per-million prices at the top, and prints cost per call and cost for 10,000 calls.
# Concepts: cost per transaction, the number a business actually asks for. Input and
#   output are priced differently, so they are multiplied separately and only then
#   divided by 1,000,000 (the divisor is exercise D3's bug). Prices are placeholders -
#   put your own model's rates in before quoting a figure.
# How to run: python 08_cost_per_transaction.py

import os
import requests

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ["MODEL_ENDPOINT"],
    "X-Model-Key": os.environ["MODEL_KEY"],
    "X-Model-Chat-Deployment": os.environ["MODEL_DEPLOYMENT"],
}

repeats = 10
input_price_per_million = 1.0
output_price_per_million = 4.0

total_in = 0
total_out = 0
count = 0

for i in range(repeats):
    body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        usage = response.json()["usage"]
        total_in = total_in + usage["prompt_tokens"]
        total_out = total_out + usage["completion_tokens"]
        count = count + 1

if count > 0:
    average_in = total_in / count
    average_out = total_out / count
    cost_per_call = (average_in * input_price_per_million + average_out * output_price_per_million) / 1000000
    print("Average tokens in:", round(average_in))
    print("Average tokens out:", round(average_out))
    print("Cost per call:", round(cost_per_call, 6))
    print("Cost for 10,000 calls:", round(cost_per_call * 10000, 2))
else:
    print("No answers returned, so there is nothing to cost. Check the app and your variables.")
