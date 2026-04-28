# 🛒 Customer Feedback Sentiment Database
### SQL + Python Analytics Project | Real-World Business Intelligence

---

## 📁 Project Structure

```
amazon-sentiment-analysis/
│
├── amazon_sentiment_analysis.ipynb   # Main notebook (all queries + charts)
├── README.md                         # Project documentation
└── preview.png                       # Output screenshot (optional)
```

---

## 📦 Dataset Source

- **Platform:** Kaggle
- **Dataset:** Amazon Sales Dataset
- **Author:** karkavelrajaj
- **Download Method:** kagglehub (auto-downloads inside notebook)

```python
import kagglehub
path = kagglehub.dataset_download("karkavelrajaj/amazon-sales-dataset")
```

- **Raw Data Contains:** Product names, categories, ratings, review content, discount percentage, prices
- **Total Records:** 1000+ real Amazon product reviews

---

## 📓 What the Notebook Does

The notebook walks through a complete data analytics pipeline:

**Step 1 — Data Collection**
Downloads raw CSV data directly from Kaggle using kagglehub into Google Colab environment.

**Step 2 — Data Cleaning**
- Extracts main category from pipe-separated category strings
- Converts rating column to numeric format
- Handles null values and removes duplicates
- Adds sentiment label (Positive / Neutral / Negative)

**Step 3 — Database Setup**
Loads cleaned data into SQLite database and sets up SQL query environment using Pandas.

**Step 4 — SQL Insights (7 Business Queries)**
- Average rating by product category
- Low rated products (complaint detection)
- Top praised products (positive feedback)
- Sentiment distribution with percentage
- Review volume and engagement by category
- Discount impact on customer satisfaction
- Most complained categories (business alert)

**Step 5 — Data Visualization**
- Bar chart: Average rating by category
- Pie chart: Sentiment distribution
- Bar chart: Complaint count by category

---

## 👥 Who Uses / Views This Project

| Audience | Why They Care |
|---|---|
| **Recruiters** | Shows SQL + Python + business thinking in one project |
| **Data Analysts** | Real example of text + SQL analytics pipeline |
| **Business Managers** | Understand how customer feedback drives decisions |
| **Students** | Learn how to build an end-to-end analytics project |
| **Developers** | See how SQLite integrates with Python and Pandas |

---

## 💼 Real World Business Impact

This project simulates exactly what analysts do at companies like Amazon, Flipkart, Swiggy, and Zomato every day:

**Product Teams** use category sentiment trends to decide which products need quality improvements in the next version.

**Marketing Teams** use top praised products list to build campaigns and decide which products to feature on homepage.

**Customer Support Teams** use complaint detection queries to prioritize and resolve recurring issues faster.

**Pricing Teams** use discount impact analysis to understand whether heavy discounts are attracting dissatisfied customers.

**Seller Management Teams** use category-level ratings to decide which sellers to promote or penalize on the platform.

> 💡 In short — every 1-star review costs a business money. This project shows how to catch and act on that signal at scale.

---

## 🎓 What You Learn From This Project

**SQL Skills**
- Writing analytical queries on real data
- Using CASE statements for sentiment classification
- Aggregation with GROUP BY, AVG, COUNT, SUM
- Filtering with WHERE for complaints and praise
- Ordering and limiting results for business reports

**Python Skills**
- Loading and cleaning data with Pandas
- Connecting Python to SQLite database
- Building charts with Matplotlib and Seaborn
- Writing reusable functions for SQL queries

**Data Cleaning Skills**
- Handling pipe-separated string columns
- Converting data types safely
- Filling null values and dropping duplicates
- Feature engineering (creating sentiment column)

**Business Thinking Skills**
- Translating raw ratings into business decisions
- Understanding what metrics matter to real companies
- Framing data insights as business recommendations
- Building a project that tells a complete data story

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Google Colab | Development environment |
| Python 3 | Core programming language |
| Pandas | Data manipulation and cleaning |
| SQLite | Database for SQL queries |
| Matplotlib | Data visualization |
| Seaborn | Chart styling |
| kagglehub | Dataset download |

---

## ▶️ How to Run

1. Open `amazon_sentiment_analysis.ipynb` in Google Colab
2. Run all cells from top to bottom
3. Dataset downloads automatically — no manual setup needed
4. All outputs and charts generate inline in the notebook

---

## 📊 Key Insights Found

- Identified which product categories have highest and lowest customer satisfaction scores
- Found that majority of reviews are Positive (rating >= 4)
- Detected top complaint categories for business alerting
- Discovered correlation between discount level and rating
- Ranked most engaging product categories by review volume

---

*Built with Python + SQL | Dataset from Kaggle | Run on Google Colab*
