"""Module for generating and printing reports."""

from fpdf import FPDF

from src.bank_transaction_analyzer.data_filter import (
    filter_bank_number,
    filter_dates,
    filter_name,
    filter_purchase_data,
    generate_declaration_data,
)


class PDFReport(FPDF):
    """PDF Report Layout."""

    report_title = ""

    def header(self) -> None:
        """Create the header for the PDF report."""
        self.set_font("Courier", "B", 8)
        self.cell(0, 10, f"{self.report_title}", ln=True, align="L")

    def add_table(self, data: str) -> None:
        """Add a table to the PDF report."""
        self.set_font("Courier", size=6)

        for line in data.split("\n"):
            self.cell(0, 5, line, ln=True, align="L")


def generate_declaration_report() -> None:
    """Generate and print the declaration report as a PDF."""
    df = generate_declaration_data(None)

    total_km = df["Subtotal km"].sum()

    pdf = PDFReport()
    pdf.report_title = "KM Declaration Report"
    pdf.add_page()
    pdf.set_font("Courier", size=8)
    pdf.add_table(df.to_string(justify="right"))
    pdf.cell(0, 10, f"Total km: {total_km}", ln=True)
    pdf.output("km_declaration_report.pdf")
    print("Declaration report generated: km_declaration_report.pdf")


def generate_month_report(month: str) -> None:
    """Generate and print the month declaration report as a PDF."""
    df = generate_declaration_data(month)

    months = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    }
    month_name = months[month]

    total_km = df["Subtotal km"].sum()

    pdf = PDFReport()
    pdf.report_title = f"KM Declaration Report - {month_name}"
    pdf.add_page()
    pdf.set_font("Courier", size=8)
    pdf.add_table(df.to_string(justify="right"))
    pdf.cell(0, 10, f"Total km: {total_km}", ln=True)
    pdf.output("month_km_declaration_report.pdf")
    print("Declaration report generated: month_km_declaration_report.pdf")


def generate_purchase_report(shop_name: str) -> None:
    """Generate and print the purchase report as a PDF."""
    df = filter_purchase_data(shop_name)
    entries = len(df)

    pdf = PDFReport()
    pdf.report_title = f"Purchase Summary Report - {shop_name}"
    pdf.add_page()

    pdf.set_font("Courier", size=6)
    pdf.cell(0, 5, "_" * 60)
    pdf.add_table(df.to_string(index=False, justify="right"))

    pdf.cell(0, 5, "_" * 60)
    pdf.ln()
    pdf.cell(0, 5, f" Found {entries} entries", ln=True, align="L")

    pdf.output(f"{shop_name}_purchase_report.pdf")
    print(
        f"Purchase report for {shop_name} has been generated: "
        f"{shop_name}_purchase_report.pdf",
    )


def generate_date_filter_report(start_date: str, end_date: str | None) -> None:
    """Generate and print the date-specific report as a PDF."""
    df = filter_dates(start_date, end_date)
    entries = len(df)

    pdf = PDFReport()
    pdf.report_title = (
        f"Date Summary Report  {start_date} - {end_date or start_date}"
    )
    pdf.add_page()

    pdf.set_font("Courier", size=6)
    pdf.cell(0, 5, "_" * 60, ln=True)

    table = [
        ("Date", 20, "L"),
        ("Counter Party", 50, "L"),
        ("Amount", 10, "R"),
        ("IBAN", 25, "L"),
        ("Description", 100, "L"),
    ]

    for title, width, _ in table:
        pdf.cell(width, 5, title, align="L")
    pdf.ln()

    for _, row in df.iterrows():
        for title, width, align in table:
            pdf.cell(width, 5, str(row[title])[:60], align=align)
        pdf.ln()

    pdf.cell(0, 5, "_" * 60)
    pdf.ln()
    pdf.cell(0, 5, f" Found {entries} entries", ln=True, align="L")

    if end_date is None:
        pdf.output(f"{start_date}_report.pdf")
        print(
            f"A report for the dates has been generated: {start_date}_report.pdf",
        )
    else:
        pdf.output(f"{start_date}_{end_date}_report.pdf")
        print(
            "A report for the dates has been generated: "
            f"{start_date}_{end_date}_report.pdf",
        )


def generate_bank_number_results(iban: str) -> None:
    """Generate and print the bank number-specific report as a PDF."""
    df = filter_bank_number(iban)
    entries = len(df)

    pdf = PDFReport()
    pdf.report_title = f"Bank Number Search Result - ({iban})"
    pdf.add_page()
    pdf.cell(0, 5, f" Found {entries} entries", ln=True, align="L")
    pdf.ln()
    pdf.set_font("Courier", size=8)
    pdf.cell(0, 5, "_" * 60, ln=True)
    table = [
        ("IBAN", 35, "L"),
        ("Date", 20, "L"),
        ("Counter Party", 60, "L"),
        ("Amount", 15, "R"),
        ("Description", 80, "L"),
    ]

    for title, width, _ in table:
        pdf.cell(width, 5, title, align="R")
    pdf.ln()

    for _, row in df.iterrows():
        for title, width, align in table:
            pdf.cell(width, 5, str(row[title])[:35], align=align)
        pdf.ln()

    pdf.cell(0, 5, "_" * 60)
    pdf.ln()
    pdf.cell(0, 5, f" Found {entries} entries", ln=True, align="L")

    pdf.output(f"bank_number_{iban}_report.pdf")
    print(
        f"A report for bank number {iban} was generated: bank_number_{iban}_report.pdf"
    )


def generate_name_results(name: str) -> None:
    """Generate and print the name-specific report as a PDF."""
    df = filter_name(name)
    entries = len(df)

    pdf = PDFReport()
    pdf.report_title = f"Name Search Result - ({name})"
    pdf.add_page()

    pdf.set_font("Courier", size=6)

    pdf.cell(0, 5, "_" * 60, ln=True)
    table = [
        ("IBAN", 35, "L"),
        ("Name", 60, "L"),
        ("Date", 20, "L"),
        ("Amount", 15, "R"),
        ("Description", 80, "L"),
    ]

    for title, width, _ in table:
        pdf.cell(width, 5, title, align="L")
    pdf.ln()

    for _, row in df.iterrows():
        for title, width, align in table:
            pdf.cell(width, 5, str(row[title])[:35], align=align)
        pdf.ln()

    pdf.cell(0, 5, "_" * 60)
    pdf.ln()
    pdf.cell(0, 5, f" Found {entries} entries", ln=True, align="L")

    pdf.output(f"{name}_report.pdf")
    print(f"A report for {name} has been generated as: {name}_report.pdf")
