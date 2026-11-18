# Latency and percentiles

## Latency is a quality attribute

An answer that is right but arrives after 30 seconds is a failure for the user. Speed is part of quality, so we test it like anything else.

`latency_ms` in the app's response is the time the app took to answer, in milliseconds. It includes the search through the documents and the model call. It does not include the network between you and the app.

## One number is not enough

Send the same question 10 times and you get 10 different times. To describe them we use:
- **Average:** the sum divided by the count. A few very slow requests pull it up, and a few very fast ones pull it down.
- **p50 (the median):** half of the requests were faster than this. This is the typical user.
- **p95:** 95 out of 100 requests were faster than this. The unlucky 5 waited longer.
- **Slowest:** the worst case you saw.

## How the programs find the percentiles

1. Put all times in a list.
2. Sort the list from smallest to largest (`times.sort()`).
3. p50 is the item in the middle: `times[len(times) // 2]`.
4. p95 is the item 95% of the way along: `times[int(len(times) * 0.95) - 1]`.

This is a simple method. With only 10 requests, p95 is almost the slowest request. With 100 or more requests it becomes steadier. Always say how many requests a number is based on.

## The tail

The slow requests are called the tail. Users remember the tail. A service with a good average and a bad p95 gets complaints. That is why Level 3 asks for percentiles and not just an average.

## What makes latency vary

- The length of the answer. The model writes one token at a time, so longer answers take longer.
- The length of the question and retrieved text.
- How busy the model service is.
- Retrieval and the other work the app does.
