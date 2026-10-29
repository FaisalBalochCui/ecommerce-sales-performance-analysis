# E-commerce Sales & Business Performance Analytics

## Project Overview
This project analyzes retail sales data to understand revenue, profit, customer activity, product-category performance, regional trends, and monthly performance. It demonstrates a Python-based workflow for transforming raw data into business KPIs, reports, and visualizations.

## Business Questions
- Which product categories generate the most revenue and profit?
- How do sales and profits change over time?
- Which regions contribute most to business performance?
- What relationship, if any, exists between discounts and profit?

## Dataset
The file `data/sales_orders.csv` contains synthetic retail data created for portfolio demonstration. It does not represent a real company or actual customer transactions.

## Tools & Technologies
- Python
- pandas
- Data validation and date processing
- Matplotlib
- CSV reporting and data visualization

## Key Results
The analysis generated the following summary:

| Metric | Result |
|---|---:|
| Orders | 850 |
| Customers | 324 |
| Total revenue | 231,119.35 |
| Total profit | 77,704.49 |
| Profit margin | 33.62% |
| Average order value | 271.91 |
| Average discount | 6.10% |

**Currency:** The dataset does not specify a currency, so monetary values are presented without a currency symbol.

## Key Findings
- **Furniture** generated the highest revenue and profit among the listed categories.
- **Technology** ranked second in revenue and profit.
- **Office Supplies** had the highest order count but the lowest revenue among the listed categories. Its order values could be investigated further.
- The discount-versus-profit chart supports exploratory analysis, but it does not establish that discounts cause changes in profit.

These findings describe the synthetic dataset only and should not be interpreted as real-world business conclusions.

## Project Workflow
1. Load and validate the sales dataset.
2. Process dates and prepare data for analysis.
3. Calculate revenue, profit, order, customer, and discount KPIs.
4. Analyze monthly, category, and regional performance.
5. Explore the relationship between discounts and profit.
6. Export summary tables and charts.

## Generated Outputs

### CSV Reports
- `outputs/kpi_summary.csv`
- `outputs/monthly_performance.csv`
- `outputs/category_performance.csv`
- `outputs/region_performance.csv`

### Visualizations
- `outputs/monthly_revenue.png`
- `outputs/category_profit.png`
- `outputs/discount_vs_profit.png`

## How to Run
Run these commands from the project directory:

```bash
python -m pip install -r requirements.txt
python src/run_analysis.py
```

Python must be installed on your computer. These commands install the required libraries and run the analysis.

## Possible Next Steps
- Reproduce the KPIs using SQL.
- Build an interactive dashboard in Power BI or Tableau.
- Investigate outliers and discount patterns.
- Add automated tests for data validation and calculations.

## Project Limitations
This project uses synthetic data for learning and portfolio demonstration. Results are useful for demonstrating analytical methods, not for making decisions about a real business.