
# km_declaration *(working title, subject to rename)*

**km_declaration** is a Python backend project that processes transaction exports from **Rabobank** to generate useful business reports. It identifies and counts transactions at specific locations, calculates estimated driven kilometers for travel declarations, and can produce detailed purchase summaries — including PDF reports.

This project started as an internal tool for a snackbar where I work, and is now shared as part of my **junior backend developer portfolio** to demonstrate pragmatic data processing and automation skills.

---

## 📌 Project Summary

* **Language:** Python
* **Domain:** Transaction data processing / reporting
* **Input:** CSV exports from Rabobank
* **Output:** Summaries, statistics, and PDF reports
* **Status:** Active development (features growing over time)

---

## 🧠 What It Does

This tool helps you:

* 💾 Load Rabobank CSV transaction exports
* 📍 Filter transactions for specific shops or terminals
* 📊 Count purchases per location
* 🚗 Estimate driven kilometers based on purchase frequency
* 📄 Generate PDF summaries of results
* 🛠 Future capability: more reporting and formats

---

## 🛠️ Technologies Used

* 🐍 **Python 3**
* 📊 **pandas** for data processing
* 📄 PDF generation library (fpdf)
* CSV file handling and text encoding
