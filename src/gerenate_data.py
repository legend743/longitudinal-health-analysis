import pandas as pd
import numpy as np

np.random.seed(42)

# -----------------------------
# 1. Patient information
# -----------------------------

patients = pd.DataFrame({
    "patient_id": range(1001, 1101),
    "age": np.random.randint(25, 70, 100),
    "gender": np.random.choice(
        ["Male", "Female", "male", "F", "M"],
        100
    )
})

# Add some invalid/missing values
patients.loc[5, "age"] = np.nan
patients.loc[15, "age"] = 150
patients.loc[25, "gender"] = None

patients.to_csv("data/raw/patients.csv", index=False)


# -----------------------------
# 2. Visit information
# -----------------------------

records = []

for patient_id in range(1001, 1101):

    baseline_weight = np.random.normal(70, 10)

    for visit_number in range(1, 5):

        visit_date = pd.Timestamp("2025-01-01") + pd.DateOffset(
            months=(visit_number - 1) * 3
        )

        weight = baseline_weight + np.random.normal(0, 2)

        bmi = weight / (1.7 ** 2)

        glucose = np.random.normal(120, 20)

        systolic_bp = np.random.normal(130, 15)

        records.append([
            patient_id,
            visit_number,
            visit_date,
            round(weight, 2),
            round(bmi, 2),
            round(glucose, 2),
            round(systolic_bp, 2)
        ])

visits = pd.DataFrame(
    records,
    columns=[
        "patient_id",
        "visit_number",
        "visit_date",
        "weight",
        "bmi",
        "glucose",
        "systolic_bp"
    ]
)

# Add missing values
visits.loc[10, "bmi"] = np.nan
visits.loc[50, "glucose"] = np.nan
visits.loc[100, "weight"] = np.nan

# Add an invalid value
visits.loc[150, "glucose"] = -20

# Add duplicate
visits = pd.concat(
    [visits, visits.iloc[[20]]],
    ignore_index=True
)

visits.to_csv("data/raw/visits.csv", index=False)


# -----------------------------
# 3. Treatment information
# -----------------------------

treatments = pd.DataFrame({
    "patient_id": range(1001, 1101),
    "treatment": np.random.choice(
        ["Treatment A", "Treatment B", "Control"],
        100
    )
})

treatments.to_csv("data/raw/treatments.csv", index=False)


print("Datasets created successfully!")