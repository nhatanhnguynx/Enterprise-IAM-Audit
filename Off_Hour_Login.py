import pandas as pd
# ==============================================================================
# AUDIT BLOCK: DIGITAL FORENSIC INGESTION PIPELINE
# PROJECT: ENTERPRISE IAM & TEMPORAL ANOMALY DETECTION ENGINE
# STEP: CONTROL TESTING FOR ITGC ACCESS MANAGEMENT (ZERO TRUST ALIGNMENT)
# ==============================================================================


# 1. DATA INGESTION: Extracting Active Directory user authentication logs from local Data Lakehouse
print("[INFO] Ingesting Cloud IAM login logs from corporate repository...")
df = pd.read_csv('C:/Users/nhata/Desktop/python/Audit_Login_Logs.csv')

# 2. DATA TYPE SANITIZATION: Cast raw string timestamps into standardized Pandas Datetime objects
# This enables high-performance vectorized operations on seasonal/temporal attributes
df['Login_Timestamp'] = pd.to_datetime(df['Login_Timestamp'])

# 3. FORENSIC MASK DEFINITION: Establishing the high-risk operational window
# Target: Capturing anomalies executing between 00:00:00 (Midnight) and 05:59:59 (Before Dawn)
# Evaluates .dt.hour component natively to prevent iterative loop processing overhead
Times_Mask = ((df['Login_Timestamp'].dt.hour >= 0) & (df['Login_Timestamp'].dt.hour <= 5) ).copy()

# 4. EXCEPTION ISOLATION: Implementing absolute data integrity protocols
# Applying Vectorized Boolean Masking to isolate unauthorized off-hour access events
# Employs explicitly defined .copy() to decouple the slice from the source immutable dataframe
Off_Hour_Login = df[Times_Mask].copy()

# 5. DATA COMPLIANCE EXPORT: Generating target operational artifact for C-Level Reporting
# Outputs isolated risk indicators to Excel format while suppressing the metadata index column
print("[SUCCESS] Anomaly detection complete. Exporting Exception Report for Executive review...")
Off_Hour_Login.to_excel('Off_Hour_Logins.xlsx', index = False)
# ==============================================================================
# END OF FORENSIC SCRIPT - DATA ARTIFACTS SUCCESSFULLY GENERATED
# ==============================================================================