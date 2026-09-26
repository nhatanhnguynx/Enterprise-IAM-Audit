import pandas as pd

#df_master = pd.read_csv('C:/Users/nhata/Desktop/python/HR_Master_Data.csv')
df_cloud = pd.read_csv('C:/Users/nhata/Desktop/python/Cloud_IAM_Users.csv')

#merge_hr_cloud = pd.merge(df_master, df_cloud, on = 'Employee_ID')
#Ghost_Accounts_Report = merge_hr_cloud[(merge_hr_cloud['HR_Status'] == 'TERMINATED') & 
#(merge_hr_cloud['IT_Status'] == 'ACTIVE')]
#print(Ghost_Accounts_Report)
#Ghost_Accounts_Report.to_excel('Ghost_Accounts_Report.xlsx', index = False)
df_cloud['Last_Login'] = pd.to_datetime(df_cloud['Last_Login'])
moc_thoi_gian = pd.Timestamp.now() - pd.Timedelta(days=90)
Dormant_Accounts_Report = df_cloud[(df_cloud['IT_Status'] == 'ACTIVE') & (df_cloud['Last_Login'] < moc_thoi_gian )].copy()

print(Dormant_Accounts_Report )

Dormant_Accounts_Report.to_excel('Dormant_Accounts_Report.xlsx', index=False)