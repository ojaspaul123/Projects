
# 🧢 Jockey Distribution Report 2024
### Complete Data Analysis & Visualization using Python

---

## 📌 Project Overview

This project performs end-to-end data analysis on the **Chirag Paul Jockey Distributor 2024** sales dataset. It covers data cleaning, filtering, manipulation, and **20+ visualizations** built using Matplotlib, Seaborn, and Plotly — all inside a single Jupyter Notebook.

---

## 📁 Project Files

```
📦 Project Folder
 ┣ 📓 chirag_paul_jockey_full_visualization.ipynb   ← Main Jupyter Notebook
 ┣ 📄 ChiragPaul_Jockey_Distributor_2024.csv        ← Raw input dataset
 ┗ 📄 ChiragPaul_Jockey_2024_Cleaned.csv            ← Cleaned output dataset (auto-generated)
```

---

## 🗂️ Dataset Description

| Column | Description |
|---|---|
| `Transaction_ID` | Unique transaction identifier |
| `Order_ID` | Order reference number |
| `Order_Date` | Date the order was placed |
| `Delivery_Date` | Date the order was delivered |
| `Month` / `Quarter` | Time period of the transaction |
| `Distributor_Name` | Name of distributor (Chirag Paul) |
| `Distributor_Location` | Location of distributor |
| `Retailer_ID` / `Retailer_Name` | Retailer details |
| `Retailer_Area` / `Retailer_Type` | Retailer location and type |
| `Request_Channel` | How the order was placed (Phone, Email, WhatsApp, etc.) |
| `Section` | Product category (Inner Wear - Men/Women, Essentials, etc.) |
| `SKU_Code` / `Product_Name` | Product identifier and name |
| `Qty_Requested` / `Qty_Supplied` | Quantities ordered vs fulfilled |
| `Unit_Dist_Price_INR` / `MRP_per_Unit_INR` | Pricing details |
| `Gross_Amount_INR` / `Net_Amount_INR` | Amount before/after discount |
| `Discount_Percent` / `Discount_Amount_INR` | Discount applied |
| `GST_Percent` / `GST_Amount_INR` | Tax details |
| `Invoice_Amount_INR` | Final billed amount |
| `Order_Status` | Fulfilled / Pending Delivery / Partially Fulfilled / Backordered |
| `Payment_Mode` | Cheque / COD / UPI / Credit |
| `Payment_Status` | Paid / Due (Pending) / Partially Paid |
| `Remarks` | Additional notes |

---

## 🛠️ Libraries & Installation

```bash
pip install pandas numpy matplotlib seaborn plotly
```

| Library | Version | Purpose |
|---|---|---|
| `pandas` | ≥ 1.3 | Data loading, cleaning, manipulation |
| `numpy` | ≥ 1.21 | Numerical operations |
| `matplotlib` | ≥ 3.4 | Static charts (Bar, Line, Pie, Scatter, etc.) |
| `seaborn` | ≥ 0.11 | Statistical visualizations (Heatmap, Violin, KDE, etc.) |
| `plotly` | ≥ 5.0 | Interactive charts (Sunburst, Treemap, Funnel, etc.) |

---

## 📓 Notebook Structure

### Step 1 — 📦 Import Libraries
Imports all required libraries and sets global chart styles and display settings.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
```

---

### Step 2 — 📂 Load Data
Loads the CSV dataset and previews structure using `.head()`, `.info()`, and `.describe()`.

```python
df = pd.read_csv('ChiragPaul_Jockey_Distributor_2024.csv')
```

---

### Step 3 — 🧹 Data Cleaning

| Task | Action |
|---|---|
| Missing values | `Payment_Status` → filled with `'Unknown'`; `Remarks` → filled with `'No Remarks'` |
| Date columns | Converted `Order_Date` & `Delivery_Date` to `datetime` |
| Numeric columns | Enforced with `pd.to_numeric()` |
| Whitespace | Stripped from all string columns |
| Duplicates | Detected and removed with `drop_duplicates()` |
| Column rename | `Invoice_Amount_INR` → `Invoice_Amt`, etc. |

---

### Step 4 — 🔍 Data Filtering

Five filtered subsets created for targeted analysis:

| Filter | Condition |
|---|---|
| `df_fulfilled` | `Order_Status == 'Fulfilled'` |
| `df_disc` | `Discount_Percent > 0` |
| `df_unpaid` | `Payment_Status` is `'Due (Pending)'` or `'Partially Paid'` |
| `df_highval` | `Invoice_Amt > 50,000` |
| `df_q4` | `Quarter == 'Q4'` |

---

### Step 5 — 🔧 Data Manipulation

New computed columns added to the dataset:

| New Column | Formula / Logic |
|---|---|
| `Delivery_Days` | `Delivery_Date - Order_Date` (in days) |
| `Fulfillment_Rate` | `(Qty_Supplied / Qty_Requested) × 100` |
| `Profit_Margin` | `(Invoice_Amt - Net_Amt) / Invoice_Amt × 100` |
| `Retailer_City` | Extracted from `Retailer_Area` (text before comma) |
| `Revenue_Band` | Low / Medium / High based on `Invoice_Amt` threshold |

Aggregated summary tables also created: `monthly_rev`, `section_rev`, `quarter_rev`, `top_retailers`, `sec_delivery`, and more.

---

## 📊 Visualizations

### 🖼️ Matplotlib Charts (10)

| # | Chart Type | Description |
|---|---|---|
| MPL-1 | **Bar Chart** | Monthly Revenue with Q1–Q4 color coding |
| MPL-2 | **Grouped Bar** | Section-wise Orders vs Revenue (dual-axis) |
| MPL-3 | **Barh Chart** | Top 10 Retailers by Revenue |
| MPL-4 | **Barh Chart** | Average Delivery Days by Section |
| MPL-5 | **Pie Chart** | Section Revenue Share |
| MPL-6 | **Pie + Donut** | Payment Status & Request Channel (side-by-side) |
| MPL-7 | **Line Chart** | Monthly Revenue & Qty Supplied Trend (dual-axis) |
| MPL-8 | **Scatter Plot** | Qty Supplied vs Invoice Amount by Section |
| MPL-9 | **Stacked Area** | Quarterly Revenue by Section |
| MPL-10 | **Histogram** | Distribution of Invoice Amount & Delivery Days |

---

### 🎨 Seaborn Charts (8)

| # | Chart Type | Description |
|---|---|---|
| SNS-1 | **Heatmap** | Revenue (₹M) by Quarter × Section pivot |
| SNS-2 | **Countplot** | Order Status count grouped by Section |
| SNS-3 | **Boxplot** | Invoice Amount distribution by Section |
| SNS-4 | **Violin Plot** | Delivery Days spread by Quarter |
| SNS-5 | **Bar Charts** | Avg Invoice by Retailer Type & Revenue by Payment Mode |
| SNS-6 | **Correlation Heatmap** | Correlations among all numeric features |
| SNS-7 | **Strip Plot** | Invoice Amount per Quarter, colored by Section |
| SNS-8 | **KDE Plot** | Invoice Amount density curves by Quarter |

---

### 🚀 Plotly Interactive Charts (10)

| # | Chart Type | Description |
|---|---|---|
| PLOTLY-1 | **Bar Chart** | Interactive Monthly Revenue with hover |
| PLOTLY-2 | **Grouped Bar** | Section Revenue by Quarter (interactive) |
| PLOTLY-3 | **Dual-axis Line** | Monthly Revenue vs Qty Supplied |
| PLOTLY-4 | **Pie Chart** | Section Revenue Share (interactive) |
| PLOTLY-5 | **Donut Chart** | Payment Status Breakdown |
| PLOTLY-6 | **Bubble Scatter** | Qty Supplied vs Invoice, sized by amount |
| PLOTLY-7 | **Sunburst** | Revenue drill-down: Quarter → Section → Retailer Type |
| PLOTLY-8 | **Treemap** | Revenue by Section & Retailer Type |
| PLOTLY-9 | **Funnel Chart** | Order Status pipeline (Fulfilled → Backordered) |
| PLOTLY-10 | **Box Plot** | Interactive Invoice Amount distribution by Section |

---

## ▶️ How to Run

1. Clone or download this repository
2. Place `ChiragPaul_Jockey_Distributor_2024.csv` in the same folder as the notebook
3. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```
4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook chirag_paul_jockey_full_visualization.ipynb
   ```
5. Run all cells: **Kernel → Restart & Run All**

---

## 📤 Output

After running the notebook, a cleaned dataset is automatically exported:

```
ChiragPaul_Jockey_2024_Cleaned.csv
```

This file includes all original columns plus the newly engineered features: `Delivery_Days`, `Fulfillment_Rate`, `Profit_Margin`, `Retailer_City`, and `Revenue_Band`.

---

## 📈 Key Metrics (from dataset)

| Metric | Value |
|---|---|
| Total Transactions | 1,138 rows |
| Total Columns | 32 (+ 5 engineered) |
| Date Range | January 2024 – December 2024 |
| Product Sections | 6 |
| Order Statuses | 4 (Fulfilled, Pending Delivery, Partially Fulfilled, Backordered) |
| Payment Modes | 5 (Cheque, COD, UPI/NEFT, Credit 15/30 Days) |
| Request Channels | 5 (Phone Call, In-Person, Email, WhatsApp, Written Order Form) |

---

## 👤 Author

**Chirag Paul**
Jockey Distributor — Agartala, Tripura
Data Analysis Project — 2024

---

## 📜 License

This project is for educational and business analysis purposes only.
