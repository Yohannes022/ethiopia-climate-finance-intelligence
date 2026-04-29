# 🇪🇹 Ethiopia Climate Finance & Carbon Market Readiness Intelligence System

## 📌 Project Overview

This project is a **data-driven climate finance intelligence system** designed to analyze Ethiopia’s climate finance landscape and assess its readiness for participation in global carbon markets under Article 6 of the Paris Agreement.

The system integrates real-world datasets, performs multi-layer analysis, and produces policy-relevant insights to support decision-making ahead of COP32.

---

## 🎯 Objectives

* Analyze climate finance flows to Ethiopia (2015–2024)
* Identify donor dependencies and sector allocation patterns
* Evaluate climate finance alignment (adaptation vs mitigation)
* Assess carbon market readiness
* Model future scenarios for climate finance growth
* Generate policy recommendations and strategic insights

---

## 🧠 System Architecture

This project is structured into five key layers:

1. **Data Engineering Layer**

   * Multi-year OECD CRS dataset ingestion (2015–2024)
   * Chunk-based processing for large-scale data
   * Data cleaning, normalization, and transformation

2. **Data Processing & Feature Engineering**

   * Climate tagging (Adaptation vs Mitigation)
   * Sector mapping
   * Donor and recipient structuring

3. **Analytics Layer**

   * Climate finance trends
   * Donor dependency analysis
   * Sector distribution analysis
   * Climate finance alignment

4. **Forecasting & Scenario Modeling**

   * Time-series forecasting using Prophet
   * Scenario simulations:

     * Business-as-usual
     * Policy improvement
     * Carbon market expansion

5. **Policy Intelligence Layer**

   * Carbon Market Readiness Score
   * Risk analysis (dependency, misalignment)
   * Policy recommendations aligned with COP32

---

## 📊 Key Insights

* Climate finance is growing (~8.7% annually)
* High donor concentration (~70% from top 2 donors)
* Only ~13% of funding is climate-targeted
* Significant funding directed to emergency response
* Adaptation-focused financing dominates over mitigation

---

## 🔮 Scenario Insights

* **Business-as-usual:** Growth continues but structural issues persist
* **Policy improvement:** Better alignment improves outcomes
* **Carbon market expansion:** Increased mitigation boosts readiness

---

## 🧮 Carbon Market Readiness Score

A composite score (0–100) based on:

* Climate finance inflow trends
* Climate alignment
* Donor diversification
* Sector distribution

👉 Result: **~49 / 100 (Moderate readiness)**

---

## 📊 Dashboard

A Streamlit dashboard was developed to visualize:

* Climate finance trends
* Donor contributions
* Sector allocation
* Scenario comparisons
* Readiness score

Run locally:

```bash
streamlit run dashboard/app.py
```

---

## 📁 Data Sources

* OECD DAC CRS (Climate Finance)
* Global climate datasets (multi-year)
* National policy references (Ethiopia CRGE)

---

## ⚙️ Tech Stack

* Python (Pandas, NumPy)
* Data Visualization (Matplotlib, Plotly)
* Forecasting (Prophet)
* Dashboard (Streamlit)
* Data Storage (Parquet)

---

## 🚀 Key Features

* Scalable data pipeline (chunk processing)
* Real-world policy-oriented analysis
* Scenario modeling for decision support
* End-to-end system (data → insight → policy)

---

## 📄 Outputs

* Policy Briefing (COP32 aligned)
* Climate Finance Analysis
* Scenario Modeling Results
* Interactive Dashboard

---

## 👤 Author

Yohannes Tesfaye

---

## 📌 Note

This project is designed as a **policy intelligence prototype**, demonstrating how data science can support climate finance strategy, carbon market participation, and international policy decision-making.
