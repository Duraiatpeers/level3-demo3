# Tokens and cost

## What a token is

A token is a piece of text, roughly four characters in English. The model charges for tokens, in two parts:
- **Tokens in (prompt tokens):** everything sent to the model: the hidden instructions, the retrieved chunks and the question.
- **Tokens out (completion tokens):** the answer the model writes.

The app returns both in `usage`. This is the number the provider bills, not an estimate.

## Cost per transaction

One transaction is one question and answer.

cost = (tokens in x input price + tokens out x output price) / 1,000,000

Prices are quoted per million tokens, and output tokens normally cost more than input tokens. Use the price list for your own model and region.

`08_cost_per_transaction.py` averages 10 calls and then projects the cost for 10,000 calls. The two prices in the file are example numbers. Replace them.

## Where the tokens come from

In a RAG application the tokens in are mostly not the question:
- the hidden instructions (the prompt version),
- the retrieved chunks (how many, and how long),
- earlier turns in the same session.

So a change to the prompt or to retrieval changes the cost of every question.

## Cost regression

A cost regression is a change that makes the same work cost more without anyone deciding it should. Examples: a longer prompt, more retrieved chunks, a model upgrade. To catch it:
1. Measure the baseline (average tokens and cost per call).
2. Set a budget a little above the baseline.
3. Test against that budget every time something changes.

`10_cost_regression_test.py` shows the idea. The budget numbers in it are generous starting values. Set yours from your own baseline.
