# Longitudinal Patient Health Data Analysis

## Overview
This project demonstrates a data science workflow for analyzing synthetic longitudinal patient health data collected across repeated visits.

## Objectives
- Clean and preprocess multiple datasets.
- Merge patient, visit, and treatment information.
- Perform exploratory data analysis (EDA).
- Visualize glucose distributions and trends over time.
- Apply descriptive statistics and ANOVA.
- Engineer baseline and glucose-change features.
- Train and evaluate a Logistic Regression classification model.
- Document data processing and perform data-quality checks.

## Technologies
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- SciPy
- Scikit-learn
- Jupyter Notebook
- Git and GitHub

## Project Structure
- `data/raw/` — synthetic source datasets
- `notebooks/` — data cleaning and analysis notebook
- `src/` — data-generation script
- `figures/` — exported visualizations
- `tables/` — descriptive statistics tables
- `docs/` — data dictionary and cleaning log

## How to Run
1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Open the notebook in Jupyter or VS Code.
5. Run the notebook cells in order.

## Example Results
- 100 synthetic patients.
- 400 visit records after duplicate removal.
- A glucose trend figure across four visits and three treatment groups.
- A Logistic Regression model evaluated using accuracy, precision, recall, and a confusion matrix.

## Limitations
The dataset is synthetic and is used for educational purposes only. The model's results are not clinical findings and must not be used for medical decisions. The small test set also limits the reliability of the reported performance metrics.
