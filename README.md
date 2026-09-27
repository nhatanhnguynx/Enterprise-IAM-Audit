# 🛡️ Enterprise IAM Audit & Data Analytics Suite

# 🛡️ Enterprise IAM Audit & Data Analytics Suite

## 📌 Executive Summary
An automated, Python-based audit engine designed to identify Identity and Access Management (IAM) anomalies, Segregation of Duties (SoD) conflicts, and behavioral risks across massive enterprise datasets (50,000+ records)

Built to replace manual audit testing with **Pandas Vectorization**, reducing testing time from days to milliseconds. Aligned with **SOC 2** and **ISO 27001** Access Control compliance requirements

---

## ⚙️ Core Audit Modules

### 1. Ghost & Dormant Account Hunter (`iam_audit_engine.py`)
* **Risk:** Terminated employees retaining active system access; unmonitored inactive accounts.
* **Algorithm:** Reconciles HR Master Data with Cloud IAM logs. Utilizes Boolean Masking and Datetime vectors to detect active ghosts and accounts dormant for >90 days

### 2. Segregation of Duties (SoD) Conflict Engine (`sod_audit_engine.py`)
* **Risk:** Fraud via toxic role combinations (e.g., `ROLE_CREATE_VENDOR` + `ROLE_APPROVE_PAYMENT`)
* **Algorithm:** Performs relational Inner Joins (`pd.merge`) across 80,000+ role assignments to flag exact accounts violating SoD policies.

### 3. Off-Hour Anomaly Detection (`off_hour_audit.py`)
* **Risk:** Unauthorized systemic access or potential data exfiltration during non-business hours.
* **Algorithm:** Time-series filtering of login timestamps to isolate midnight/unauthorized access (00:00 - 05:00)

### 4. Privilege Creep Scanner (`privilege_creep.py`)
* **Risk:** Users accumulating excessive permissions over time without revocation, violating the Principle of Least Privilege (PoLP).
* **Algorithm:** Applies `.groupby().count()` aggregation to identify users exceeding the maximum allowable role threshold (>3 roles)

---

## 🛠️ Tech Stack & Methodology
* **Language:** Python 3.x
* **Core Library:** Pandas (DataFrames, GroupBy, Merging, Datetime Analytics)
* **Performance:** O(N) vectorized operations capable of processing Enterprise-scale Big Data without memory overflow.

> *"Designed to mass-clear dormant access and terminate ghost accounts before they even realize it 🦠"*
## 💡 The Audit Mindset (NhatAnhNguyen's Note)
> *"The codebase in this repository may appear minimalist if viewed purely through the lens of traditional software development. However, when evaluated against Enterprise Audit standards, this simplicity is highly intentional. In Tech Risk, true value lies not in the complexity of the code, but in its **Business Impact**—the ability to utilize precision algorithms to uncover critical vulnerabilities and enforce compliance across massive datasets in milliseconds"*

peace  ❤️ love ur guys 
