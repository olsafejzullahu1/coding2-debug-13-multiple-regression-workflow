# Multiple Regression and Workflow Design — Debugging Practice

Coding 2 homework, companion to **Lecture 13: Multiple Regression and Workflow Design**.

## The project

`analysis.ipynb` predicts `salary_k_eur` from career attributes in
`data/career_outcomes.csv`, following the workflow from the lecture:

1. Fit a one-predictor baseline and a multiple-regression model and describe their fit.
2. Compare the two models out of sample, using a train/test split, to decide whether the
   extra predictors are worth keeping.
3. Plot predicted vs. actual salaries for the multiple model.

## Your task

This project does not yet work the way it should. Clone it, get it running, and read it
critically: make sure every step actually does what it claims to do and that the
conclusions it reaches are justified. Fix whatever you find.

Work like an analyst reviewing a colleague's notebook — at each step, ask where this could
go wrong and whether you believe the numbers.

You may use an LLM to help, but treat its suggestions as drafts: check them against the
data and against what the lecture says a sound workflow looks like.

## Running it

```bash
uv sync
uv run jupyter lab        # open analysis.ipynb and run it top to bottom
```

To execute the whole notebook from the command line:

```bash
uv run jupyter nbconvert --to notebook --execute analysis.ipynb --stdout
```

## Data

`data/career_outcomes.csv` is a small synthetic teaching dataset; no downloads are needed.
