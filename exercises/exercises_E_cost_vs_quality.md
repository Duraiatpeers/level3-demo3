# Exercises: Cost Without Losing Quality

**E1. Compare versions**
Run `09_compare_versions.py`. Fill in the table.

| Version | Correct | Average tokens | Average ms |
|---|---|---|---|
| v1 | | | |
| v2 | | | |
| v2_1 | | | |

Which version is cheapest? Which is cheapest and still correct?

**E2. More questions**
Add two questions of your own to `checks` in `09_compare_versions.py`, each with the word that must appear in a correct answer. Does the result change?

**E3. Bigger sample**
Change `repeats` to 5. Does the ranking of the versions stay the same?

**E4. Set a budget**
Run `10_cost_regression_test.py` once with the budgets as they are. Then set `token_budget` to 1.2 times the average tokens you saw in D4 and run it again. Does it still pass?

**E5. Caching**
Ask the same question 5 times with `02_ten_timings.py`. The app has no cache. If it had one, what would happen to latency and cost on the second to fifth request? What would happen to your test results, and why might that be a problem?

**E6. Think**
A change makes every answer 30% cheaper and 2 of 15 correct answers become wrong. Do you accept it? Write the decision and the reason.
