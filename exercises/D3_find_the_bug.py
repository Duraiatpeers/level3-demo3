# D3_find_the_bug.py - exercise D3, Topic D (see exercises_D_cost.md)
# What it does: works out cost per call from fixed token counts, with no API call at all.
#   It prints a cost that is 1000 times too high.
# Concepts: unit errors are the most common cost-reporting mistake, and they are never
#   caught by the program crashing. Prices are per million tokens - check the divisor,
#   then compare with solutions/D3_fixed.py. Sense-check the output: a per-call cost of
#   nearly a dollar for one short answer should look wrong immediately.
# How to run: python D3_find_the_bug.py

import requests

url = "http://localhost:8000/ask"
headers = {"X-API-Key": "your-key-here"}

total_in = 900
total_out = 40
input_price_per_million = 1.0
output_price_per_million = 4.0

cost_per_call = (total_in * input_price_per_million + total_out * output_price_per_million) / 1000

print("Cost per call:", cost_per_call)
print("Cost for 10,000 calls:", cost_per_call * 10000)
