"""Reproduce the supplied teaching extract from an unchanged Homework 1 CSV.

This is a maintainer utility. Students use the committed data/career_outcomes.csv.
It reads a local input file and never downloads data or restores missing values.
"""

import argparse
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


SOURCE_SHA256 = "5190bfe1ed75060f30aa8b3e8f13cb02656fbef7766cb25e95243801a214e798"
ROOT = Path(__file__).resolve().parents[1]


def prepare(source: Path, output: Path) -> None:
    if source.resolve() == output.resolve():
        raise ValueError("The original input and prepared output must be different files.")
    if hashlib.sha256(source.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError("Input does not match the documented Homework 1 source CSV.")

    workers = pd.read_csv(source)
    # Simulate unavailable experience records for a defined subset of workers.
    missing_experience = workers["experience_years"].ge(8) & workers["training_hours"].lt(35)
    # Simulate separately unavailable education records with a fixed random draw.
    rng = np.random.default_rng(2026)
    missing_education = rng.random(len(workers)) < 0.10

    workers.loc[missing_experience, "experience_years"] = np.nan
    workers["education_years"] = workers["education_years"].astype("Int64")
    workers.loc[missing_education, "education_years"] = pd.NA
    output.parent.mkdir(parents=True, exist_ok=True)
    workers.to_csv(output, index=False, lineterminator="\n")
    print(f"Wrote {len(workers)} rows to {output}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Local, unchanged Homework 1 career_outcomes.csv")
    parser.add_argument("--output", type=Path, default=ROOT / "data/career_outcomes.csv")
    args = parser.parse_args()
    prepare(args.source, args.output)
