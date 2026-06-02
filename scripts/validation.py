import pandas as pd

# =========================================================
# OPENSTREETMAP ROAD NETWORK VALIDATION SYSTEM
# =========================================================

# =========================================================
# LOAD DATASET
# =========================================================

roads = pd.read_csv(
    "roads.csv",
    low_memory=False
)

print("\n=================================================")
print("DATASET INFORMATION")
print("=================================================")

print(f"Dataset Shape: {roads.shape}")

total_records = len(roads)

print(f"Total Road Segments: {total_records}")


# =========================================================
# DATA VALIDATION RESULTS
# =========================================================

print("\n=================================================")
print("DATA VALIDATION RESULTS")
print("=================================================")


# ---------------------------------------------------------
# VALIDATION 1: MISSING ROAD NAMES
# ---------------------------------------------------------

missing_name = roads["name"].isna().sum()

print(f"Missing Road Names: {missing_name}")


# ---------------------------------------------------------
# VALIDATION 2: MISSING HIGHWAY TYPE
# ---------------------------------------------------------

missing_highway = roads["highway"].isna().sum()

print(f"Missing Highway Type: {missing_highway}")


# ---------------------------------------------------------
# VALIDATION 3: MISSING SPEED LIMITS
# ---------------------------------------------------------

missing_speed = roads["maxspeed"].isna().sum()

print(f"Missing Speed Limits: {missing_speed}")


# ---------------------------------------------------------
# VALIDATION 4: MISSING LANE INFORMATION
# ---------------------------------------------------------

missing_lanes = roads["lanes"].isna().sum()

print(f"Missing Lane Information: {missing_lanes}")


# ---------------------------------------------------------
# VALIDATION 5: MISSING WIDTH INFORMATION
# ---------------------------------------------------------

missing_width = roads["width"].isna().sum()

print(f"Missing Width Information: {missing_width}")


# ---------------------------------------------------------
# VALIDATION 6: DUPLICATE RECORDS
# ---------------------------------------------------------

duplicates = roads.duplicated().sum()

print(f"Duplicate Records: {duplicates}")


# ---------------------------------------------------------
# VALIDATION 7: INVALID ROAD LENGTHS
# ---------------------------------------------------------

invalid_length = (
    roads["length"] <= 0
).sum()

print(f"Invalid Road Lengths: {invalid_length}")


# =========================================================
# TOTAL VALIDATION ERRORS
# =========================================================

total_errors = (
    missing_name +
    missing_highway +
    missing_speed +
    missing_lanes +
    missing_width +
    duplicates +
    invalid_length
)

print(f"\nTotal Validation Errors: {total_errors}")


# =========================================================
# WEIGHTED DATA QUALITY SCORE
# =========================================================

missing_name_pct = (
    missing_name / total_records
) * 100

missing_highway_pct = (
    missing_highway / total_records
) * 100

missing_speed_pct = (
    missing_speed / total_records
) * 100

missing_lanes_pct = (
    missing_lanes / total_records
) * 100

missing_width_pct = (
    missing_width / total_records
) * 100

duplicate_pct = (
    duplicates / total_records
) * 100

invalid_length_pct = (
    invalid_length / total_records
) * 100


weighted_penalty = (

    missing_highway_pct * 0.30 +

    missing_name_pct * 0.25 +

    missing_speed_pct * 0.15 +

    missing_lanes_pct * 0.15 +

    missing_width_pct * 0.05 +

    duplicate_pct * 0.05 +

    invalid_length_pct * 0.05

)

quality_score = max(
    0,
    round(
        100 - weighted_penalty,
        2
    )
)

print("\n=================================================")
print("WEIGHTED DATA QUALITY SCORE")
print("=================================================")

print(f"Quality Score: {quality_score}%")


# =========================================================
# CREATE VALIDATION SUMMARY TABLE
# =========================================================

summary = pd.DataFrame({

    "Metric": [

        "Total Road Segments",
        "Missing Road Names",
        "Missing Highway Type",
        "Missing Speed Limits",
        "Missing Lane Information",
        "Missing Width Information",
        "Duplicate Records",
        "Invalid Road Lengths",
        "Total Validation Errors",
        "Weighted Quality Score"

    ],

    "Value": [

        total_records,
        missing_name,
        missing_highway,
        missing_speed,
        missing_lanes,
        missing_width,
        duplicates,
        invalid_length,
        total_errors,
        quality_score

    ]

})


# =========================================================
# EXPORT VALIDATION SUMMARY
# =========================================================

summary.to_csv(
    "validation_summary.csv",
    index=False
)

print("\nValidation summary exported successfully.")


# =========================================================
# EXPORT CLEANED DATASET
# =========================================================

cleaned_roads = roads.drop_duplicates()

cleaned_roads = cleaned_roads[
    cleaned_roads["length"] > 0
]

cleaned_roads.to_csv(
    "cleaned_roads.csv",
    index=False
)

print("Cleaned dataset exported successfully.")


# =========================================================
# COMPLETED
# =========================================================

print("\n=================================================")
print("ROAD NETWORK VALIDATION COMPLETED")
print("=================================================")