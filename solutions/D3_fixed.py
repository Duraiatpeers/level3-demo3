# D3_fixed.py - solution to exercise D3, Topic D
# What it does: the corrected version of exercises/D3_find_the_bug.py - divides by
#   1,000,000 instead of 1,000, so the cost matches per-million pricing.
# Concepts: the fix is one zero count. Same arithmetic as 08_cost_per_transaction.py, with
#   fixed token numbers so the maths can be checked without calling the app.
# How to run: python D3_fixed.py

import requests

url = "http://localhost:8000/ask"
headers = {"X-API-Key": "your-key-here"}

total_in = 900
total_out = 40
input_price_per_million = 1.0
output_price_per_million = 4.0

cost_per_call = (total_in * input_price_per_million + total_out * output_price_per_million) / 1000000

print("Cost per call:", cost_per_call)
print("Cost for 10,000 calls:", cost_per_call * 10000)
