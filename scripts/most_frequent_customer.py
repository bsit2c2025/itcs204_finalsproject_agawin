"""
Utility to find most frequent customer name(s) in a CSV dataset.

Usage:
    python most_frequent_customer.py ../Amazon.csv --top 3

This prints the top customer names and their frequencies.
"""
from __future__ import annotations

import argparse
import os
import sys
from typing import Tuple

import pandas as pd


def get_top_customers(csv_path: str, column: str = "CustomerName", top_n: int = 1, case_insensitive: bool = True) -> pd.Series:
    """Return the top N customer names and their frequencies.

    Args:
        csv_path: Path to CSV file containing the dataset.
        column: Column name that contains customer names.
        top_n: Number of top entries to return.
        case_insensitive: Normalize case so 'John Doe' and 'john doe' are counted together.

    Returns:
        A pandas Series mapping customer name -> frequency, sorted descending.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")
    df = pd.read_csv(csv_path)
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in CSV. Available columns: {', '.join(df.columns)}")
    names = df[column].astype(str).str.strip()
    if case_insensitive:
        names = names.str.title()
    vc = names.value_counts()
    return vc.head(top_n)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Find most frequent customer names in a CSV file")
    parser.add_argument("csv", help="Path to CSV file")
    parser.add_argument("--col", default="CustomerName", help="Column name containing customer names")
    parser.add_argument("--top", type=int, default=1, help="Number of top customer names to print")
    parser.add_argument("--no-normalize", action="store_true", help="Disable case normalization/stripping")
    args = parser.parse_args(argv)
    try:
        top = get_top_customers(args.csv, column=args.col, top_n=args.top, case_insensitive=not args.no_normalize)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
    print(top.to_string())


if __name__ == "__main__":
    main()
