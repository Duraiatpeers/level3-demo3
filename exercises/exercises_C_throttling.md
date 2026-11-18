# Exercises: Throttling

Ask your trainer before you run the biggest levels. Every request uses the shared model quota.

**C1. Find the limit**
Run `06_find_throttling.py`. At which number of workers did throttled requests first appear? If none appeared, write that down.

**C2. Slow or failing**
Compare a run where latency was high with a run where requests failed. In one sentence each, say what the user sees.

**C3. Retry**
Write a program that sends one request and, if the answer contains `429` in the text, waits 2 seconds with `time.sleep(2)` and tries again, up to 3 times. Print how many tries it took.

**C4. Think**
When the model is throttled, what should the user see? Choose one and say why:
- a long error message from the server,
- a blank answer,
- a short message saying the service is busy and to try again.
What would your test check?
