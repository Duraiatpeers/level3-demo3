# Answers: Module 3.3

**A1 and A2.** Longer answers take longer because the model writes more tokens. Numbers differ between runs. The average moves less than p95, because p95 depends on the few slowest requests.

**A3.** The list must be sorted before you pick a position in it. Add `times.sort()` before the p95 line. See `A3_fixed.py`.

**A5.** An average of 2 seconds can hide a few very slow requests. A customer remembers those. Check p95 (and p99 for large volumes), and look at the slowest requests.

**B1 and B2.** Running requests at the same time is faster, but not in a straight line: the model service handles only so many at once. Doubling workers rarely halves the time.

**B3.** `seconds = time.time() - start` runs before the requests, so it measures nothing. Move it after the `with` block. See `B3_fixed.py`.

**B4.** p95 usually rises faster than p50, because waiting requests queue up and the unlucky ones wait longest.

**B5.** For example: the rate limit (quota) of the model deployment; what a user does during a peak; how long a user will wait; whether the app and network can handle the load as well.

**C1 to C2.** Slow means the user waits and still gets an answer. Failing means the user gets an error. They need different fixes: capacity for slow, retry and a clear message for failing.

**C3.** See `C3_retry.py`.

**C4.** The short "service is busy, try again" message. A test would check that the status or message tells the user what to do, and that no internal details (stack traces, keys) appear.

**D3.** One million is `1000000`, not `1000`. See `D3_fixed.py`.

**D4.** Input tokens are usually the bigger number because they include the retrieved chunks and the hidden instructions. Output tokens usually cost more per token. Which effect wins depends on your numbers, and checking them is the point.

**D5.** Retrieving more chunks (a higher top_k), or longer chunks, raises tokens in for every question.

**E1 to E3.** Results depend on your run. The point is to choose the cheapest version that still gets the required answers right, and to check that the ranking holds with a larger sample.

**E4.** A budget set exactly at the current number will fail from small variation. Set a margin, and move it only on purpose.

**E5.** A cache would make the second to fifth requests faster and cheaper. Tests that repeat one question would then measure the cache and not the model, so the numbers would look better than a user's real experience. Use varied questions, or switch the cache off, for model tests.

**E6.** There is no single answer. A defensible position names the threshold in advance (for example, no loss in correct answers), so the decision follows from the rule and not from the saving. Two correct answers lost is a quality regression and would normally not be accepted for a saving.
