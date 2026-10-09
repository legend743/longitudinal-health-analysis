# Data Dictionary — Longitudinal Patient Health Analysis

## Project Overview
This project uses a synthetic dataset to demonstrate data cleaning, exploratory data analysis, statistical analysis, and longitudinal health data analysis.

## Dataset Variables

| Variable | Description | Data Type |
|---|---|---|
| patient_id | Unique identifier for each patient | Integer |
| visit_number | Patient visit number (1–4) | Integer |
| visit_date | Date of the patient visit | Date |
| age | Patient age in years | Numeric |
| gender | Patient gender category | Categorical |
| treatment | Assigned group: Control, Treatment A, or Treatment B | Categorical |
| weight | Patient weight in kilograms | Numeric |
| bmi | Body Mass Index | Numeric |
| glucose | Measured glucose level | Numeric |
| systolic_bp | Systolic blood pressure | Numeric |
| baseline_glucose | Patient's glucose value at the first visit | Numeric |
| glucose_change | Difference between current and baseline glucose | Numeric |
| final_glucose | Glucose value at Visit 4, used for the prediction exercise | Numeric |
| high_glucose | Binary target: 1 if final glucose is at least 126, otherwise 0 | Binary |

## Data Structure
- Patients dataset: 100 unique patients.
- Visits dataset: 400 visit records after duplicate removal.
- Treatments dataset: treatment assignment for each patient.
- Analysis dataset: one row per patient visit, with patient information and treatment assignment.

## Important Note
All patient records are synthetic and were generated for educational purposes. They do not represent real patients or clinical findings.