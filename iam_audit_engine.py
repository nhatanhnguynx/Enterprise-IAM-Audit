import pandas as pd


df_cloud = pd.read_csv('C:/Users/nhata/Desktop/python/Cloud_IAM_Users.csv')

df_cloud['Last_Login'] = pd.to_datetime(df_cloud['Last_Login'])

Time_Line = pd.Timestamp.now() - pd.Timedelta(days=90)

Dormant_Accounts_Report = df_cloud[(df_cloud['IT_Status'] == 'ACTIVE') & (df_cloud['Last_Login'] < moc_thoi_gian )].copy()

print(Dormant_Accounts_Report )

Dormant_Accounts_Report.to_excel('Dormant_Accounts_Report.xlsx', index=False)