# 📊 E2E-Retail-Sales-Analysis-SQL-Python-PowerBI

_Analyzing retail sales, returns, and customer behavior to improve business performance using SQL, Python, and Power BI._


<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning & Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#kpi-analysis--key-insights">KPI Analysis & Key Insights</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendations">Final Recommendations</a>
- <a href="#future-work">Future Work</a>
- <a href="#author--contact">Author & Contact</a>

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project performs an end-to-end analysis of retail sales and return data to uncover insights into business performance, customer behavior, and product efficiency.

The pipeline includes:
- Data ingestion and cleaning  
- Exploratory Data Analysis (EDA)  
- KPI computation  
- Visualization and dashboard creation  

The goal is to support **data-driven decision-making** and improve profitability.

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Retail businesses face several operational challenges:

- High product return rates affecting revenue  
- Lack of visibility into sales performance  
- Difficulty identifying top-performing products  
- Limited understanding of customer purchasing behavior  
- No structured insights for decision-making  

This project aims to solve these using analytics and visualization.

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- Online Retail Dataset (UCI Repository)  
- ~541,909 records  
- 8 columns  

### Key Features:
- InvoiceNo, StockCode, Description  
- Quantity (negative values indicate returns)  
- UnitPrice  
- CustomerID  
- Country  
- InvoiceDate  

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- Python (Pandas, NumPy)  
- Matplotlib & Seaborn  
- SQL  
- Power BI  
- Jupyter Notebook  

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
retail-sales-analysis/
│
├── README.md
├── requirements.txt
├── Project_Report.pdf
│
├── data/
│ └── online_retail.csv
│
├── notebooks/
│ └── analysis.ipynb
│
├── sql/
│ └── queries.sql
│
├── dashboard/
│ └── Sales_Analysis_Dashboard.pbix
│
├── images/
│ └── dashboard.png

```
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="data-cleaning--preparation"></a>Data Cleaning & Preparation</h2>

- Removed missing values and duplicates  
- Handled outliers using IQR method  
- Created new features:
  - Revenue = Quantity × UnitPrice  
  - YearMonth for trend analysis  
- Separated sales and return transactions  
- Cleaned invalid or negative entries  

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

**Key Observations:**

- Large number of transactions with negative quantities → returns  
- Skewed distribution in quantity and price  
- Seasonal patterns in monthly sales  
- High variation in return trends  

**Outliers Identified:**
- Extremely high quantities (bulk purchases or returns)  
- High-value pricing outliers  

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="kpi-analysis--key-insights"></a>KPI Analysis & Key Insights</h2>

### 📊 Core KPIs:
- Total Sales Quantity: ~2.84M  
- Total Return Quantity: ~76K  
- Total Orders: ~19K  
- Total Customers: ~4.1K  
- Gross Revenue: ~5.39M  
- Return Rate: ~2.7%  

### 🔍 Insights:
- Strong sales with seasonal peaks  
- Return rate impacts profitability  
- Few products contribute to most returns  
- UK dominates sales region  
- High-value customers drive major revenue  
- Higher price reduces demand (price sensitivity)  

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="dashboard"></a>Dashboard</h2>

Power BI dashboard provides:
- Sales vs Return Trends  
- Top Selling Products  
- Most Returned Products  
- Customer Insights  
- Country-wise Analysis  

<div align="center"> <img src="https://github.com/GauravDhamne/E2E-Online-Retail-Sales-Data-Analysis-Project-SQL-Python-PowerBI/blob/main/Images/retail_sales_dashboard.png.png" alt="PowerBI Dashboard"> </div>

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/your-username/retail-sales-analysis.git
```

2. Install Dependencies:
```bash
pip install pandas numpy matplotlib seaborn
```

3. Run Jupyter Notebook:
```bash
Ingestion_DB.ipynb
File-1-Data_Preperation.ipynb
File-2-Data_Visualiztion.ipynb
File-3-KPI_Analysis.ipynb
```

4. Open Power BI Dashboard:
```
dashboard/Sales_Analysis_Dashboard.pbix
```
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>

- Improve product quality to reduce returns
- Focus on high-return products for corrective action
- Optimize pricing strategies
- Target high-value customers for retention
- Improve inventory management
- Expand into high-performing regions

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="future-work"></a>Future Work</h2>

- Build predictive models for sales and returns
- Perform customer segmentation (RFM analysis)
- Develop real-time dashboards
- Apply machine learning for return prediction
- Integrate customer feedback data

<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

Gaurav Dhamne


📧 Email: gauravdhamne5@gmail.com

🔗 LinkedIn: http://linkedin.com/in/gɑurɑv-dhɑmne-14a4aa281

💻 GitHub: https://github.com/GauravDhamne
