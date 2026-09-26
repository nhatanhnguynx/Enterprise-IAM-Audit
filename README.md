# 🛡️ Enterprise IAM Audit Engine (JML Lifecycle)

*Automated IT General Controls (ITGC) & Identity Governance using Python (Pandas)*

## 📌 Executive Summary
This project automates the reconciliation of Human Resources (HR) Master Data against Cloud Infrastructure Identity Access Management (IAM) logs (simulating an environment of 200,000+ records). It programmatically detects **Ghost Accounts** (Terminated but Active) and **Dormant Accounts** using vectorization and boolean masking in Pandas.

## ⚙️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy
- **Techniques:** Data Merging (Inner Joins), Datetime Vectorization, Boolean Masking

## 📊 Audit Exception Report (The 4C's)

### 1. Criteria
According to the Corporate Information Security Policy (Section 4.2 - User Access Lifecycle Management), all system user accounts must be deactivated or terminated within 24 hours upon the employee's official termination date from the HR master database

### 2. Condition
Data reconciliation between the HR Master Data and Cloud IAM logs revealed that **208 terminated employees** still maintained "ACTIVE" user accounts on the corporate cloud infrastructure, long after their departure dates. Additionally, **4,284 accounts** were identified as dormant (no login activity for >90 days)

### 3. Cause
There is a lack of automated integration and communication channels between the Human Resources (HR) department and the Information Technology (IT) identity management team. The off-boarding checklist was processed manually, leading to omissions in access revocation.

### 4. Effect
Unauthorized access to sensitive corporate cloud environments could be exploited by former employees or external threat actors using these orphan accounts. This exposes the organization to severe risks of data exfiltration, system sabotage, and non-compliance with SOC 2 requirements

---
*Developed as part of the Tech Risk & Data Forensic Architecture portfolio*
