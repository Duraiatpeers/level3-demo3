# 07_tokens_per_call.py - Topic D (tokens and cost), handout 03
# What it does: sends one question and prints the tokens read in (prompt_tokens), the
#   tokens written back (completion_tokens) and the total, from the usage field.
# Concepts: tokens are the unit you are billed in. Input is usually far larger than
#   output in a RAG app, because the system prompt and the retrieved chunks all count as
#   input - that is where cost work pays off. A KeyError on "usage" means the app is the
#   older version without the usage change.
# How to run: python 07_tokens_per_call.py

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

if response.status_code != 200:
    print("No answer returned. Status:", response.status_code)
    print("Body:", response.text)
else:
    usage = response.json()["usage"]
    print("Tokens sent in:", usage["prompt_tokens"])
    print("Tokens written back:", usage["completion_tokens"])
    print("Total:", usage["prompt_tokens"] + usage["completion_tokens"])
