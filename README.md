<div align="center">

![BlueMart Logo](assets/logo.png)

# BlueMart Retail LLC — 2025 Analytics Project Story

**Transforming Retail Through Data-Driven Insights**

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0-green.svg)](https://pandas.pydata.org/)

</div>

---

## 📊 Company Overview

**BlueMart Retail LLC** is a UAE-based omnichannel retailer operating **50 stores** across Dubai, Abu Dhabi, and Sharjah, complemented by a robust e-commerce presence via its website, mobile app, and leading marketplaces such as Amazon.ae and Noon.

- **Products**: ~200 SKUs across Grocery, Beverages, Personal Care, Household, Snacks, Dairy, and Electronics
- **Customers**: ~5,000 unique customers in 2025, segmented into loyalty tiers (Silver, Gold, Platinum)
- **Objective**: Integrate physical and digital channels, optimize inventory, and leverage analytics for actionable business decisions

---

## 🎯 Business Challenge

BlueMart faces typical mid-sized retailer challenges in the competitive UAE market:

- **Inventory Management**: Maintain optimal stock levels across 50 stores despite SKU rotation, slow movers, and seasonal spikes (Ramadan, Black Friday, Dubai Shopping Festival)
- **Demand Forecasting**: Predict SKU-level demand to prevent stockouts or overstock situations
- **Customer Behavior**: Understand purchasing patterns and channel preferences for retention and targeted campaigns
- **Channel Performance**: Evaluate performance across store, website, mobile, and marketplaces for revenue optimization
- **Promotion ROI**: Assess promotional effectiveness and seasonal impact on margins
- **Data Quality**: Handle real-world complications including missing customer IDs, stockouts, and inconsistent discount application

---

## 💡 Project Goal

Build a **KPI-driven analytics framework** to:

✅ Provide holistic visibility into sales, inventory, promotions, and customer behavior  
✅ Identify high-value customers and preferred channels  
✅ Enable management to make data-driven decisions improving revenue, gross margin, and operational efficiency  
✅ Deliver insights via executive-ready dashboards and reports

---

## 📈 Dataset Overview

| Aspect | Details |
|--------|---------|
| **Time Period** | Jan 1 – Dec 31, 2025 (daily granularity) |
| **Stores** | 50 stores (Mall, High Street, Community) |
| **SKU Universe** | 200 SKUs across 7 categories |
| **Customers** | ~5,000 registered customers |
| **Channels** | Store, Website, Mobile App, Amazon.ae, Noon |
| **Transaction Volume** | **11.4M sales records** |

### Data Tables

| Table | Description | Size |
|-------|-------------|------|
| **Store Master** | store_id, store_name, city, store_type, opening_date | 50 rows |
| **SKU Master** | sku_id, sku_name, category, subcategory, unit_price, cost_price, brand | 200 rows |
| **Customer Master** | cust_id, age, gender, city, loyalty_segment, registration_date | ~5,000 rows |
| **Sales Transactions** | date, store_id, sku_id, customer_id, quantity, unit_price, total_value, channel, discount_pct | **11.4M rows** |
| **Inventory Snapshot** | store_id, sku_id, stock_on_hand, reorder_point, snapshot_date | ~5,000 rows |
| **Promotions** | promo_id, promo_name, start_date, end_date, discount_pct, promo_type | ~9 rows |

---

## 🔑 Key Performance Indicators (KPIs)

### Executive Summary Metrics

<div align="center">

| KPI | 2025 Performance | Insight |
|-----|------------------|---------|
| **Total Revenue** | **AED 1.03 Billion** | Strong omnichannel performance |
| **Gross Margin** | **31.0%** | Healthy profitability across categories |
| **Total Units Sold** | **22.9M units** | High transaction volume |
| **Avg Transaction Value** | **AED 90.00** | Consistent basket size |
| **Avg Profit per Order** | **AED 27.93** | Effective pricing strategy |

</div>

![KPI Dashboard](assets/kpi_overview.png)
*Figure 1: Executive KPI Dashboard - 2025 Performance Overview*

---

## 📊 Channel Performance Analysis

### Revenue Distribution by Channel

Our omnichannel strategy shows strong performance across all touchpoints:

| Channel | Revenue Share | Strategic Importance |
|---------|---------------|---------------------|
| **Store** | 43.5% | Core revenue driver, customer experience hub |
| **Website** | 26.6% | Growing digital presence, 24/7 availability |
| **Mobile App** | 17.4% | Convenience-focused, younger demographics |
| **Amazon.ae** | 8.7% | Marketplace expansion, new customer acquisition |
| **Noon** | 3.9% | Regional marketplace presence |

![Channel Distribution](assets/channel_distribution.png)
*Figure 2: Revenue Distribution Across Sales Channels*

### Key Insights:
- **Physical stores remain dominant** but digital channels (Website + Mobile) account for **44%** of revenue
- **Mobile app growth** indicates successful digital transformation
- **Marketplace channels** (Amazon.ae + Noon) contribute **12.6%**, providing incremental reach

---

## 🛍️ Category Performance

### Revenue by Product Category

![Category Performance](assets/category_performance.png)
*Figure 3: Sales Performance by Product Category*

| Category | Performance Rank | Strategic Focus |
|----------|------------------|-----------------|
| **Electronics** | 🥇 #1 | High-margin category, premium positioning |
| **Snacks** | 🥈 #2 | High-frequency purchases, impulse buying |
| **Household** | 🥉 #3 | Essential goods, consistent demand |
| **Grocery** | #4 | Staple category, customer retention |
| **Dairy** | #5 | Fresh products, supply chain optimization |
| **Personal Care** | #6 | Brand loyalty opportunities |
| **Beverages** | #7 | Seasonal variations, promotion-sensitive |

### Category Insights:
- **Electronics leads** in revenue contribution despite lower transaction frequency
- **Snacks and Household** show consistent performance across all channels
- **Grocery and Dairy** are key traffic drivers with high basket attachment rates

---

## 📅 Seasonal Trends & Promotions

### Monthly Revenue Trends

![Monthly Trends](assets/monthly_trends.png)
*Figure 4: Monthly Revenue Trends with Promotional Periods*

### Promotional Impact Analysis

| Promotion Period | Type | Revenue Uplift | Key Categories |
|------------------|------|----------------|----------------|
| **Ramadan Sale** (Apr) | Religious | **+50%** | Grocery, Beverages, Dairy |
| **Summer Sale** (Jul) | Seasonal | **+15%** | Personal Care, Beverages |
| **Black Friday** (Nov) | Retail Event | **+35%** | Electronics, Household |

### Key Findings:
- **Ramadan** drives the highest revenue spike, particularly in FMCG categories
- **Black Friday** shows strong performance in Electronics and Household
- **Promotional periods** account for **~40%** of annual revenue despite being only **~25%** of days

---

## 🎯 Customer Insights

### Loyalty Segmentation

![Loyalty Segments](assets/loyalty_segments.png)
*Figure 5: Customer Distribution by Loyalty Tier*

| Loyalty Tier | Customer % | Avg Transaction Value | Strategic Action |
|--------------|------------|----------------------|------------------|
| **Platinum** | 10% | AED 150+ | VIP experiences, exclusive previews |
| **Gold** | 30% | AED 100-150 | Targeted promotions, upgrade incentives |
| **Silver** | 60% | AED 60-100 | Engagement campaigns, loyalty building |

### Customer Behavior Patterns:
- **Platinum customers** generate **~35%** of revenue despite being only **10%** of the base
- **Channel preference**: Platinum customers favor Mobile App and Website for convenience
- **Basket composition**: Higher-tier customers purchase more Electronics and Premium brands

---

## 🏪 Store Performance

### Geographic Distribution

![Store Performance](assets/store_performance_map.png)
*Figure 6: Store Performance by City and Type*

| City | Stores | Revenue Contribution | Avg Store Revenue |
|------|--------|---------------------|-------------------|
| **Dubai** | 25 | 50% | AED 20.6M |
| **Abu Dhabi** | 15 | 30% | AED 20.6M |
| **Sharjah** | 10 | 20% | AED 20.6M |

### Store Type Analysis:

| Store Type | Count | Performance Characteristics |
|------------|-------|----------------------------|
| **Mall** | 20 stores | High footfall, premium categories, weekend peaks |
| **High Street** | 20 stores | Consistent traffic, convenience-focused, local loyalty |
| **Community** | 10 stores | Essential goods, frequent purchases, neighborhood hub |

---

## 💰 Profitability Analysis

### Gross Margin by Category

![Margin Analysis](assets/margin_by_category.png)
*Figure 7: Gross Margin % by Product Category*

| Category | Gross Margin % | Margin Health |
|----------|----------------|---------------|
| **Electronics** | 38-42% | 🟢 Excellent |
| **Personal Care** | 35-40% | 🟢 Strong |
| **Household** | 28-32% | 🟡 Good |
| **Snacks** | 25-30% | 🟡 Moderate |
| **Grocery** | 20-25% | 🟡 Competitive |
| **Beverages** | 18-22% | 🟠 Thin |
| **Dairy** | 15-20% | 🟠 Low |

### Profitability Insights:
- **Electronics and Personal Care** drive margin expansion
- **FMCG categories** (Grocery, Beverages, Dairy) operate on thinner margins but drive traffic
- **Promotional periods** reduce margins by **5-8%** but increase volume by **35-50%**

---

## 🚀 Key Insights & Findings

### 1. Omnichannel Success
> **Digital channels now represent 44% of revenue**, validating our omnichannel investment. Mobile app adoption is particularly strong among younger, high-value customers.

### 2. Seasonal Opportunities
> **Ramadan and Black Friday account for 25% of annual revenue**. Strategic inventory planning and targeted promotions during these periods yield exceptional ROI.

### 3. Category Mix Optimization
> **Electronics delivers highest margins (40%) while Grocery drives traffic**. Balanced category mix ensures both profitability and customer retention.

### 4. Customer Lifetime Value
> **Top 10% of customers (Platinum tier) generate 35% of revenue**. Personalized engagement and exclusive benefits for this segment show strong retention rates.

### 5. Store Format Performance
> **Mall stores outperform in Electronics and Premium categories**, while Community stores excel in daily essentials. Format-specific merchandising strategies are effective.

---

## 📋 Strategic Recommendations

### For Sales & Marketing Team

#### 1. **Channel-Specific Strategies**
- **Mobile App**: Implement push notifications for flash sales and personalized offers
- **Website**: Enhance product discovery with AI-powered recommendations
- **Marketplaces**: Expand SKU range on Amazon.ae and Noon to capture incremental demand

#### 2. **Promotional Optimization**
- **Focus on high-impact periods**: Ramadan, Black Friday, and Dubai Shopping Festival
- **Category-specific promotions**: Electronics during Black Friday, FMCG during Ramadan
- **Loyalty-based discounts**: Tiered promotions to incentivize Silver → Gold → Platinum upgrades

#### 3. **Customer Retention**
- **Platinum tier**: Exclusive early access to new products and sales
- **Gold tier**: Targeted promotions to increase basket size and frequency
- **Silver tier**: Engagement campaigns to build loyalty and upgrade potential

### For Inventory & Supply Chain Team

#### 1. **Demand Forecasting**
- **Implement SKU-level forecasting** for top 20% of products (80/20 rule)
- **Seasonal stock planning**: 50% inventory increase for Ramadan, 35% for Black Friday
- **Safety stock optimization**: Higher buffers for fast-moving Electronics and Snacks

#### 2. **Inventory Turnover**
- **Target**: 8-10 turns per year for FMCG, 4-6 for Electronics
- **Slow-mover management**: Quarterly clearance sales for bottom 10% SKUs
- **Fresh product optimization**: Daily replenishment for Dairy, twice-weekly for Grocery

#### 3. **Store-Specific Allocation**
- **Mall stores**: Higher allocation of premium and impulse categories
- **Community stores**: Focus on daily essentials and convenience items
- **High Street**: Balanced mix with emphasis on local preferences

### For Executive Leadership

#### 1. **Revenue Growth Opportunities**
- **Digital expansion**: Target 50% digital revenue share by 2026 (currently 44%)
- **Marketplace growth**: Expand to additional platforms and increase SKU range
- **Geographic expansion**: Consider new store openings in high-performing cities

#### 2. **Margin Enhancement**
- **Private label development**: Launch BlueMart-branded products in high-margin categories
- **Category mix optimization**: Increase Electronics and Personal Care share
- **Promotional efficiency**: Reduce discount depth while maintaining volume through targeted offers

#### 3. **Customer Experience**
- **Omnichannel integration**: Enable buy-online-pickup-in-store (BOPIS)
- **Loyalty program enhancement**: Gamification and experiential rewards
- **Personalization**: AI-driven product recommendations across all channels

#### 4. **Operational Excellence**
- **Inventory optimization**: Reduce stockouts by 30% through better forecasting
- **Supply chain efficiency**: Negotiate better terms with top suppliers
- **Data-driven decision making**: Expand analytics capabilities to real-time dashboards

---

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

## 📝 License

This project is for educational and portfolio purposes.

---

## 👤 Author

**[Your Name]**  
Data Analyst | Retail Analytics Specialist  
[LinkedIn](https://linkedin.com/in/yourprofile) | [Portfolio](https://yourportfolio.com) | [Email](mailto:your.email@example.com)

---

<div align="center">

**Built with ❤️ for data-driven retail excellence**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

</div>
