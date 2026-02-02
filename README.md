# Bank Transaction Analyzer

**Bank Transaction Analyzer** is a Python-based backend project that processes transaction exports from **Rabobank** to analyze, filter, and report on financial transaction data.

The application allows users to search transactions by  **IBAN**,  **counterparty name**, and  **date**, generate summaries for specific shops or locations, estimate driven kilometers based on transaction frequency, and export reports as  **PDF files** .

This project was originally developed for **private workplace use** (a snackbar) and is now maintained as part of my  **junior backend developer portfolio** , demonstrating practical data processing, reporting, and automation skills in Python.

> **Status:** Actively developed — new features and reports are added over time as the project evolves.

## 🎯 What Problem Does This Solve?

Small businesses often rely on manual processes to analyze bank transactions for reporting, bookkeeping, or travel cost declarations. Raw CSV exports from banks are difficult to interpret and reuse.

This project automates that workflow by turning raw bank data into  **structured, searchable, and readable reports** .

## 📌 Project Summary

* **Language:** Python
* **Domain:** Transaction data processing / reporting
* **Input:** CSV exports from Rabobank
* **Output:** Summaries, statistics, and PDF reports
* **Status:** Active development (features growing over time)

## 🚀 Features

* Load Rabobank transaction CSV exports
* Search transactions by:
  * IBAN
  * Counterparty name
  * Shop / location
  * Date range
* Generate summaries of purchases per shop
* Estimate driven kilometers based on transaction frequency
* Export reports to:
  * Console output
  * PDF files
* Designed as a reusable backend-style tool

## 🛠️ Technologies Used

* 🐍 Python 3
* 📊 pandas (data processing)
* 📄 PDF generation (e.g. reportlab / fpdf)
* CLI-based interface (argparse)

---

## ▶️ Usage

Bank Transaction Analyzer is a **command-line tool** for analyzing Rabobank transaction CSV exports and generating financial reports.

The application supports filtering transactions by  **name** ,  **IBAN** , and  **date range** , and can generate declaration-style reports based on the filtered data.

At least one filtering or report-related option is recommended.

Use --help to see available options.

```md
python main.py --help
```
