import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_DIR = BASE_DIR / "reports"

# Load weekly KPI report
weekly_kpi = pd.read_excel(REPORT_DIR / "weekly_kpi_report.xlsx")

THRESHOLD = 200000

alerts = weekly_kpi[weekly_kpi["total_sales"] < THRESHOLD]

if alerts.empty:
    print("All weeks meet performance thresholds.")
else:
    print("⚠️ ALERT: Sales below threshold")
    print(alerts)

ALERT_FILE = REPORT_DIR / "alerts_log.txt"

if not alerts.empty:
    with open(ALERT_FILE, "a") as f:
        f.write("ALERT: Sales below threshold\n")
        f.write(alerts.to_string(index=False))
        f.write("\n\n")
else:
    with open(ALERT_FILE, "a") as f:
        f.write("CHECK PERFORMED: All sales meet thresholds.\n\n")
