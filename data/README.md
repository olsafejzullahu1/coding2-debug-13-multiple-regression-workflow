# Career outcomes teaching extract

Use the supplied `career_outcomes.csv` for this homework. It contains synthetic
teaching data, not observations collected from real people. Each row represents one
synthetic worker. There is no worker identifier; the original CSV row order gives
the within-file row labels used in the notebook.

This is a modified version of the [Homework 1 dataset](https://github.com/ulrichwohak/coding2-debug-12-simple-linear-regression/blob/985b8ac9f998898d5dff490c3296581444d9847a/data/career_outcomes.csv).
Some experience and education values have been made unavailable for this exercise.
All 240 rows, their order, salaries, training hours, and other observed values are
unchanged. Blank fields denote missing values; they do not mean zero. Use this
extract as supplied rather than filling its blanks from the earlier assignment.

The analysis uses salary in thousands of euros (`salary_k_eur`), training hours
(`training_hours`), years of experience (`experience_years`), and years of education
(`education_years`). The file also retains `sector`, `remote`, `ai_tool_use`, and
`promoted` from the original teaching data; the specified models do not use them.
Do not treat these data as evidence about real workers or causal training effects.

## Construction and reproducibility

The original source has SHA-256
`5190bfe1ed75060f30aa8b3e8f13cb02656fbef7766cb25e95243801a214e798`.
The local preparation utility checks that input before making two changes:

- Experience is blank for records with at least 8 original years of experience
  and fewer than 35 training hours.
- Education is blank where a NumPy `default_rng(2026)` uniform draw is below 0.10.

This produces 28 missing experience values and 17 missing education values, with
two records missing both. No values in other columns are changed. The experience
mask is deliberately systematic; these rules are a synthetic teaching construction,
not a claim about a real data-collection process.

Students do not need to run a preparation or download step. To reproduce the extract
as a maintainer, run from the homework root with a local copy of the original file:

```bash
uv run python scripts/prepare_data.py /path/to/original/career_outcomes.csv --output /tmp/career_outcomes_prepared.csv
```

The script never modifies its input. It refuses a modified source or an output path
that would overwrite the input. The supplied extract is committed so that everyone
starts with the same records and missing values.
