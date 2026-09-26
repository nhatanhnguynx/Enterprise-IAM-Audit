import pandas as pd

# ============================================================
# Data Loading
# ============================================================

# Load Cloud RBAC role assignment data
df = pd.read_csv("Cloud_RBAC_Roles.csv")


# ============================================================
# SoD Conflict Detection
# ============================================================

# Identify accounts assigned the vendor creation role
role_create_vendor = df[
    df["Role_ID"] == "ROLE_CREATE_VENDOR"
]

# Identify accounts assigned the payment approval role
role_approve_payment = df[
    df["Role_ID"] == "ROLE_APPROVE_PAYMENT"
]

# Reconcile role assignments to identify
# accounts with conflicting access privileges
sod_violations = pd.merge(
    role_create_vendor,
    role_approve_payment,
    on="Account_ID"
)

# Display identified SoD exceptions
print(sod_violations)


# ============================================================
# Audit Evidence Export
# ============================================================

# Export the identified SoD violation population
# for audit documentation and further investigation
sod_violations.to_excel(
    "SoD_Violations.xlsx",
    index=False
)