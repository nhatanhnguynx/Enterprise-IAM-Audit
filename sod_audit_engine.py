import pandas as pd

df = pd.read_csv("Cloud_RBAC_Roles.csv")

role_create_vendor =df[df['Role_ID'] == 'ROLE_CREATE_VENDOR']
role_approve_payment = df[df['Role_ID'] == 'ROLE_APPROVE_PAYMENT']

merge_role = pd.merge(role_create_vendor, role_approve_payment, on = 'Account_ID')
print(merge_role)

merge_role.to_excel('SoD_Violations.xlsx', index = False)

