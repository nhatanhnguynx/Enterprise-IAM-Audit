import pandas as pd 

df = pd.read_csv('C:/Users/nhata/Desktop/python/Cloud_RBAC_Roles.csv')

Groupy_Account = df.groupby('Account_ID').count()
print(Groupy_Account)

privileger_creep = Groupy_Account[Groupy_Account['Role_ID'] > 3]

print(privileger_creep)