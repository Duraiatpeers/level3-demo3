# Exercises: Cost

**D1. Real prices**
Open `08_cost_per_transaction.py`. The two prices are example numbers. Replace them with the price of your model from your trainer or the Azure price list. Write down the cost per call.

**D2. Projections**
Change `10000` at the bottom of `08_cost_per_transaction.py` to 1000, then 100000. What does a day of 100000 calls cost?

**D3. Find the bug**
Run `D3_find_the_bug.py`. The cost per call is far too high. Find the wrong number and fix it.

**D4. Which side costs more?**
Run `07_tokens_per_call.py` three times. Compare tokens in and tokens out. Which side is bigger? Which side costs more per token? What does that tell you about where to save?

**D5. Think**
The retrieved chunks are part of the tokens sent in. Name one way a change to retrieval could raise the cost without changing the question.
