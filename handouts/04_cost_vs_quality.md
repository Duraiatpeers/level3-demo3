# Improving cost without losing quality

## The trap

A cheaper setup is only an improvement if answers stay correct. A version that is half the cost and gets 3 answers in 10 wrong is a loss.

## The comparison

`09_compare_versions.py` runs the same questions on each prompt version and prints:
- how many answers contained the expected words,
- average tokens,
- average latency.

Choose the cheapest version that is as correct as the current one. Decide the rule before you look at the numbers, for example "no fewer correct answers than v1".

## How good is the quality check?

The check is simple: does the expected text appear in the answer? It is quick and repeatable, and it can be wrong in both directions. A correct answer can use other words, and a wrong answer can mention the right words. Module 3.4 adds better ways to judge answers.

## Sample size

Answers vary from run to run, so a small sample can mislead. Use more repeats before you choose.

## Other ways to change cost

| Change | Effect on cost and speed | Risk to quality |
|---|---|---|
| Shorter prompt | Fewer tokens in | May lose a rule the model needed |
| Fewer retrieved chunks | Fewer tokens in | May miss the chunk with the answer |
| Smaller model | Lower price and often faster | Weaker answers on hard questions |
| Model routing (a small model for easy questions, a large model for hard ones) | Cheaper on average | A wrong routing choice sends hard questions to the weak model |
| Caching (reuse the answer to a repeated question) | Fast and almost free on a hit | Old or wrong answers can be reused, and tests may measure the cache and not the model |

For each change, measure cost, speed and quality together, on the same questions.

## Testing with a cache

If an application has a cache, repeating the same question measures the cache. Use varied questions, or turn the cache off, when you test the model.
