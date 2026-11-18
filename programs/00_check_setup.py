# 00_check_setup.py - run this first, before anything else in this module
# What it does: prints what is in your four environment variables (keys masked), then sends
#   one request to the app and prints the status code and the reply body.
# Concepts: separating "my setup is wrong" from "the app is wrong" before you start
#   measuring anything. Every other program in this module assumes this one returns 200.
# How to run: python 00_check_setup.py
#   Reading the output:
#   - NOT SET or length 0  -> that variable is missing in THIS terminal (see handout 00)
#   - Status 400           -> the app did not get a usable model endpoint, key or deployment
#   - Status 401 or 403    -> PX_API_KEY does not match the app's TRAINING_API_KEY
#   - Status 502           -> the app reached your model and the call failed; read the body
#   - Status 200           -> your setup is fine, go on to 01_one_timing.py

import os
import requests

for name in ["PX_API_KEY", "MODEL_ENDPOINT", "MODEL_KEY", "MODEL_DEPLOYMENT"]:
    value = os.environ.get(name)
    if value is None:
        print(name, "= NOT SET")
    elif "KEY" in name:
        print(name, "= length", len(value), "ending", value[-4:] if value else "(empty)")
    else:
        print(name, "= [" + value + "]")

url = "http://localhost:8000/ask"
headers = {
    "X-API-Key": os.environ.get("PX_API_KEY", ""),
    "X-Model-Endpoint": os.environ.get("MODEL_ENDPOINT", ""),
    "X-Model-Key": os.environ.get("MODEL_KEY", ""),
    "X-Model-Chat-Deployment": os.environ.get("MODEL_DEPLOYMENT", ""),
}

body = {"question": "What is the maximum operating pressure of the PX-100?", "prompt_version": "v1"}
response = requests.post(url, headers=headers, json=body)

print("Status:", response.status_code)
print("Body:", response.text[:400])
