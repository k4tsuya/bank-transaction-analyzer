"""Module for generating reports."""

from fpdf import FPDF

from src.data_generation import (
    generate_declaration_data,
    generate_purchase_data,
)


class PDFDeclarationReport(FPDF):
    """PDF Declaration Report."""

    def header(self) -> None:
        """Create the header for the PDF report."""
        self.set_font("Courier", "B", 10)
        self.cell(0, 10, "KM Declaration Report", ln=True, align="L")

    def add_table(self, data: str) -> None:
        """Add a table to the PDF report."""
        self.set_font("Courier", size=8)
        for line in data.split("\n"):
            self.cell(0, 5, line, ln=True)


def print_declaration_report() -> None:
    """Generate and print the declaration report as a PDF."""
    df = generate_declaration_data()

    total_km = df["Subtotal km"].sum()

    pdf = PDFDeclarationReport()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.add_table(df.to_string(justify="right"))
    pdf.cell(0, 5, "_" * 50, ln=True)
    pdf.cell(0, 10, f"Total km: {total_km}", ln=True)
    pdf.output("km_declaration_report.pdf")
