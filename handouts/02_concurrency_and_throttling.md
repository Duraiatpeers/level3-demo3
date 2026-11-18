# Concurrency, throttling and failing gracefully

## One user, then many

A test with one request at a time shows speed for one user. A real service has many users at once. Concurrency means several requests in flight together.

`04_sequential_vs_parallel.py` sends the same 10 requests twice: one after another, then 5 at a time. The second is faster because the waiting overlaps. The program uses `ThreadPoolExecutor`: you give it a small function and a list of jobs, and it runs several jobs at once. You do not need to know how it works inside.

## What happens as load rises

`05_load_levels.py` repeats the test with 1, 5 and 10 workers and prints p50, p95 and errors. Expect:
- Total time falls as you add workers, up to a point.
- p95 rises first. Some requests have to wait their turn.
- Eventually requests start to fail.

## Throttling

The model service gives each deployment a quota: a limit on requests and tokens per minute. When you go over it, the service answers with a 429 error ("too many requests"). In the PX app that arrives as a 502 whose text mentions 429, and `06_find_throttling.py` counts those separately from other errors.

Slow and failing are different problems:
- **Slow:** the answer comes, late. The user can wait.
- **Failing:** no answer. The user must retry or give up.

## Failing gracefully

When the service is busy, a good application:
- tells the user in plain words that it is busy and to try again,
- does not show a stack trace, keys or internal names,
- may retry a few times with a short wait, and stops after a limit,
- keeps working for other users.

A test for this checks the status and the message the user would see.

## Be careful with the shared quota

Throttling tests use real model capacity. If every learner runs the largest level at once, everyone is throttled. Follow your trainer's numbers.
