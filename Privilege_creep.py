"""
Module: Privilege Creep Scanner (IAM Analytics)
Audit Objective: Detect users accumulating excessive permissions over time, 
violating the Principle of Least Privilege (PoLP).
Audit Criteria: Users must not hold more than 3 concurrent active roles.
"""
import pandas as pd
# Step 1: Ingest Cloud IAM Role Assignment dataset
df = pd.read_csv('Cloud_RBAC_Roles.csv')
# Step 2: Aggregate role assignments per Account_ID
# Uses Pandas groupby to count the exact number of roles assigned to each user
role_count_per_account = df.groupby('Account_ID').count()
# Step 3: Flag exceptions (Privilege Creep Violations)
# Filter for accounts exceeding the maximum allowable threshold (> 3 roles)
privilege_creep_violations = role_count_per_account[role_count_per_account['Role_ID'] > 3]
# Step 4: Output Audit Findings for Review
print("--- PRIVILEGE CREEP AUDIT EXCEPTIONS ---")
print(privilege_creep_violations)
