# Data Cleaning and Processing Log

## 1. Project Overview
The project uses synthetic longitudinal patient data to demonstrate data preparation, quality control, statistical analysis, and machine learning.

## 2. Patient Data Cleaning
- Standardized gender categories, such as `male` and `M` to `Male`, and `F` to `Female`.
- Treated missing ages and ages above 100 as missing values.
- Filled missing ages using the median age.
- Filled missing gender values using the most frequent gender category.

## 3. Visit Data Cleaning
- Converted visit dates to datetime format.
- Identified and removed duplicate visit records.
- Treated negative glucose measurements as invalid and replaced them with missing values.
- Imputed missing weight, BMI, and glucose values using their respective medians.

## 4. Data Integration
- Merged visit records with patient information using `patient_id`.
- Merged treatment assignments using `patient_id`.
- Used left joins to preserve visit records during integration.

## 5. Feature Engineering
- Created `baseline_glucose` using each patient's first visit measurement.
- Created `glucose_change` by subtracting baseline glucose from the current visit glucose.
- Created `final_glucose` from Visit 4 for the prediction exercise.
- Created `high_glucose`, a binary target equal to 1 when final glucose is at least 126 and 0 otherwise.

## 6. Quality Control
After cleaning, the analysis dataset was checked for:
- Missing values
- Duplicate rows
- Expected number of visits per patient
- Invalid glucose values
- Invalid age values

The checks performed returned zero missing values, zero duplicate rows, four distinct visits per patient, zero non-positive glucose values, and zero ages outside the specified 18–100 range.

## 7. Limitations
- The dataset is synthetic and does not represent real clinical observations.
- Median imputation may affect statistical results and should be documented.
- The prediction model was trained on a small dataset and should not be used for clinical decisions.
- Results demonstrate an analytical workflow rather than validated medical findings.