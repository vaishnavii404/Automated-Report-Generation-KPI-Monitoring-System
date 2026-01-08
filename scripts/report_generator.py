import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

# Load cleaned data
df = pd.read_csv(DATA_DIR / "cleaned_data.csv", parse_dates=["date"])

print(df.head())
print(df.dtypes)

# Add week column
df["week"] = df["date"].dt.to_period("W").astype(str)

# Weekly aggregation
weekly_kpi = df.groupby("week").agg(
    total_sales=("sales_amount", "sum"),
    avg_sales=("sales_amount", "mean"),
    record_count=("sales_amount", "count")
).reset_index()

print("\nWeekly KPI:")
print(weekly_kpi)

# Ensure reports directory exists
REPORT_DIR.mkdir(exist_ok=True)

from openpyxl import load_workbook

# Ensure reports directory exists
REPORT_DIR.mkdir(exist_ok=True)

report_path = REPORT_DIR / "weekly_kpi_report.xlsx"

# Save using ExcelWriter
with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
    weekly_kpi.to_excel(writer, index=False, sheet_name="Weekly KPI")

# Auto-adjust column widths
wb = load_workbook(report_path)
ws = wb.active

for column in ws.columns:
    max_length = 0
    col_letter = column[0].column_letter
    for cell in column:
        if cell.value:
            max_length = max(max_length, len(str(cell.value)))
    ws.column_dimensions[col_letter].width = max_length + 3

wb.save(report_path)

print("Formatted weekly KPI report generated.")

