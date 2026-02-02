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

The application parses command-line arguments and generates reports based on the provided filters.

At least one filtering or report-related option is recommended.

<pre class="overflow-visible! px-0!" data-start="2249" data-end="2326"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>
</span><span>### Example commands</span><span>

```md
python main.py --name </span><span>"Snackbar Example"</span><span>
</span></span></code></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="2328" data-end="2378"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-md"><span><span>python main.py --iban NL12RABO0123456789
</span></span></code></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="2380" data-end="2474"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-md"><span><span>python main.py --name "Snackbar Example"
</span></span></code></div></div></pre>

<pre class="overflow-visible! px-0!" data-start="2476" data-end="2514"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="sticky top-[calc(var(--sticky-padding-top)+9*var(--spacing))]"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-md"><span><span>python main.py --declaration</span></span></code></div></div></pre>
