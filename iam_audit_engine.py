import pandas as pd
# ============================================================
# Configuration
# ==========================================================
# Load Cloud IAM activity dat
df_cloud = pd.read_csv('C:/Users/nhata/Desktop/python/Cloud_IAM_Users.csv')
# Normalize login timestamps for time-based analysis
df_cloud['Last_Login'] = pd.to_datetime(df_cloud['Last_Login'])
# Define the inactivity threshold for dormant accounts
DORMANT_THRESHOLD_DAYS = 90
cutoff_date = (
    pd.Timestamp.now() - pd.Timedelta(days=DORMANT_THRESHOLD_DAYS)
     )
# ============================================================
# Dormant Account Detection
# ===========================================================
# Identify active accounts with no login activity
# within the defined inactivity thresholddd

Dormant_Accounts_Report = df_cloud[(df_cloud['IT_Status'] == 'ACTIVE') & (df_cloud['Last_Login'] < cutoff_date )
]
#Display identified audit exceptions
print(Dormant_Accounts_Report )

# Export exception population for audit documentatio
Dormant_Accounts_Report.to_excel('Dormant_Accounts_Report.xlsx', index=False)