"""Simple KM declaration script."""

from numpy import var

from src.bank_transaction_analyzer.analyzer import load_bank_data
from src.bank_transaction_analyzer.cli import parse_args
from src.bank_transaction_analyzer.report_generation import (
    generate_bank_number_results,
    generate_date_filter_report,
    generate_declaration_report,
    generate_name_results,
)

if __name__ == "__main__":
    args = parse_args()

    if not any(vars(args).values()):
        print("No arguments provided. Use --help to see available options.")

    if args.input:
        bank_data = load_bank_data(args.input)
    if args.declaration:
        generate_declaration_report()
    elif args.name:
        generate_name_results(args.name)
    elif args.iban:
        generate_bank_number_results(args.iban)
    elif args.from_date and args.to_date:
        generate_date_filter_report(args.from_date, args.to_date)
