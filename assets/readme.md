## 🛠️ Technical Implementation

### Technology Stack

- **Data Generation**: Python, Pandas, NumPy
- **Data Processing**: Chunked processing for memory optimization (11.4M records)
- **Visualization**: Streamlit, Plotly
- **Analytics**: Statistical analysis, trend identification

### Project Structure

```
bluemart/
├── config.py                 # Central configuration
├── requirements.txt          # Dependencies
├── app.py                    # Streamlit Dashboard
├── scripts/
│   ├── generate_data.py      # Synthetic data generation with basket logic
│   ├── process_data.py       # Data processing pipeline
│   └── fix_sales_csv.py      # Data cleanup utility
├── data/
│   ├── raw/                  # Generated raw CSVs (11.4M records)
│   └── processed/            # Optimized data for dashboard
└── assets/                   # Visualizations and logo
```

### Key Features

- ✅ **Realistic Data Generation**: 11.4M transactions with basket correlation logic
- ✅ **Memory-Optimized Processing**: Chunked processing to handle large datasets
- ✅ **Interactive Dashboard**: Real-time filtering and drill-down capabilities
- ✅ **Scalable Architecture**: Modular design for easy extension

---

## 📊 Dashboard Preview

### Executive Overview
![Dashboard Overview](assets/dashboard_overview.png)
*Figure 8: Interactive Streamlit Dashboard - Executive View*

### Features:
- **Real-time KPI cards** with trend indicators
- **Interactive filters** by date range, channel, category, and store
- **Drill-down capabilities** from executive summary to SKU-level details
- **Export functionality** for reports and presentations

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- 8GB+ RAM (for data processing)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/bluemart.git
cd bluemart

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
# 1. Generate synthetic data (optional - data already included)
python scripts/generate_data.py

# 2. Process data for dashboard
python scripts/process_data.py

# 3. Launch dashboard
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`

---

## 📁 Deliverables

- ✅ **Cleaned & annotated dataset** (all tables, 11.4M records)
- ✅ **KPI tables & trend analysis**
- ✅ **Interactive Streamlit dashboard** (stakeholder-ready)
- ✅ **Insight report with actionable recommendations**
- ✅ **Technical documentation** for reproducibility

---

## 🎓 Use Cases

This project demonstrates:

- **Data Engineering**: Large-scale data generation and processing (11.4M records)
- **Analytics**: KPI calculation, trend analysis, and insight extraction
- **Visualization**: Executive dashboards and storytelling with data
- **Business Acumen**: Retail domain knowledge and strategic recommendations
- **Technical Skills**: Python, Pandas, Streamlit, memory optimization

Perfect for showcasing **end-to-end analytics capabilities** in portfolio presentations or hiring manager demonstrations.

---
