from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data"/"sales_orders.csv"; OUT=ROOT/"outputs"; OUT.mkdir(exist_ok=True)
def main():
    df=pd.read_csv(DATA)
    needed={"order_id","order_date","region","category","quantity","discount","revenue","profit","customer_id"}
    if not needed.issubset(df.columns): raise ValueError(f"Missing columns: {needed-set(df.columns)}")
    df["order_date"]=pd.to_datetime(df["order_date"],errors="coerce"); df=df.dropna(subset=["order_date","revenue","profit"]).copy()
    df["month"]=df.order_date.dt.to_period("M").astype(str)
    kpi=pd.DataFrame([{"orders":df.order_id.nunique(),"customers":df.customer_id.nunique(),
      "total_revenue":round(df.revenue.sum(),2),"total_profit":round(df.profit.sum(),2),
      "profit_margin_pct":round(100*df.profit.sum()/df.revenue.sum(),2),
      "average_order_value":round(df.groupby("order_id").revenue.sum().mean(),2),
      "average_discount_pct":round(100*df.discount.mean(),2)}])
    kpi.to_csv(OUT/"kpi_summary.csv",index=False)
    monthly=df.groupby("month",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),orders=("order_id","nunique"))
    monthly.to_csv(OUT/"monthly_performance.csv",index=False)
    cat=df.groupby("category",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),units=("quantity","sum"),orders=("order_id","nunique")).sort_values("profit",ascending=False)
    cat.to_csv(OUT/"category_performance.csv",index=False)
    reg=df.groupby("region",as_index=False).agg(revenue=("revenue","sum"),profit=("profit","sum"),orders=("order_id","nunique")).sort_values("revenue",ascending=False)
    reg.to_csv(OUT/"region_performance.csv",index=False)
    plt.figure(figsize=(10,5)); plt.plot(monthly.month,monthly.revenue,marker="o",label="Revenue"); plt.plot(monthly.month,monthly.profit,marker="o",label="Profit")
    plt.title("Monthly Revenue and Profit"); plt.xticks(rotation=60,ha="right"); plt.legend(); plt.tight_layout(); plt.savefig(OUT/"monthly_revenue.png",dpi=160); plt.close()
    plt.figure(figsize=(8,5)); plt.bar(cat.category,cat.profit); plt.title("Profit by Category"); plt.xticks(rotation=20,ha="right"); plt.tight_layout(); plt.savefig(OUT/"category_profit.png",dpi=160); plt.close()
    plt.figure(figsize=(7,5)); plt.scatter(df.discount*100,df.profit,alpha=.5); plt.title("Discount vs Order-Line Profit"); plt.xlabel("Discount (%)"); plt.ylabel("Profit"); plt.tight_layout(); plt.savefig(OUT/"discount_vs_profit.png",dpi=160); plt.close()
    print("KPI summary:\\n",kpi.to_string(index=False)); print("\\nCategory summary:\\n",cat.to_string(index=False)); print(f"\\nOutputs: {OUT}")
if __name__=="__main__": main()
