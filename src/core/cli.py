"""Module for parsing command-line arguments."""

import argparse


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze Rabobank transaction CSV files",
    )

    parser.add_argument(
        "--input",
        help=(
            "Loads the file of the Rabobank CSV export, by default it loads "
            "bank_data.csv"
        ),
    )

    parser.add_argument(
        "--declaration",
        action="store_true",
        help="Generate a declaration report",
    )

    parser.add_argument(
        "--month",
        help="Generate a month declaration report by proving the month number",
    )
    parser.add_argument("--name", help="Filter and generate a report by name")
    parser.add_argument("--iban", help="Filter and generate a report by IBAN")
    parser.add_argument(
        "--from-date",
        help=(
            "Filter and generate a report by Start date (YYYY-MM-DD) "
            "NOTE: This can be combined with --to-date"
        ),
    )
    parser.add_argument(
        "--to-date",
        help=(
            "Filter and generate a report by End date (YYYY-MM-DD) "
            "NOTE: This can only be used with --from-date"
        ),
    )

    return parser.parse_args()
