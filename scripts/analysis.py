import pandas as pd

# =========================================================
# LOAD DATASET
# =========================================================

roads = pd.read_csv(
    "roads.csv",
    low_memory=False
)

print("\n=================================================")
print("ROAD NETWORK ANALYSIS")
print("=================================================")


# =========================================================
# CLEAN HIGHWAY COLUMN
# =========================================================

def clean_highway(value):

    value = str(value)

    if value.startswith("["):

        value = (
            value
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
        )

        value = value.split(",")

        return value[0].strip()

    return value


roads["highway_cleaned"] = roads[
    "highway"
].apply(clean_highway)

# =========================================================
# ROAD NAME CLEANING
# =========================================================

def clean_name(value):

    # Handle missing values
    if pd.isna(value):
        return "Unnamed Road"

    value = str(value)

    # Check for list-like values
    if value.startswith("["):

        value = (
            value
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
        )

        value = value.split(",")

        return value[0].strip()

    return value


roads["name_cleaned"] = roads[
    "name"
].apply(clean_name)

# =========================================================
# ROAD TYPE DISTRIBUTION
# =========================================================

print("\n=================================================")
print("ROAD TYPE DISTRIBUTION")
print("=================================================")

road_types = (
    roads["highway_cleaned"]
    .value_counts()
)

print(road_types)

road_types.to_csv(
    "road_type_distribution.csv"
)


# =========================================================
# AVERAGE ROAD LENGTH BY TYPE
# =========================================================

print("\n=================================================")
print("AVERAGE ROAD LENGTH BY TYPE")
print("=================================================")

average_length = (
    roads
    .groupby("highway_cleaned")["length"]
    .mean()
    .sort_values(ascending=False)
)

print(average_length)

average_length.to_csv(
    "average_length_by_type.csv"
)


# =========================================================
# ONE-WAY ROAD ANALYSIS
# =========================================================

print("\n=================================================")
print("ONE-WAY ROAD ANALYSIS")
print("=================================================")

oneway_analysis = (
    roads["oneway"]
    .value_counts()
)

print(oneway_analysis)

oneway_analysis.to_csv(
    "oneway_analysis.csv"
)


# =========================================================
# BRIDGE ANALYSIS
# =========================================================

print("\n=================================================")
print("BRIDGE ANALYSIS")
print("=================================================")

bridge_analysis = (
    roads["bridge"]
    .fillna("No")
    .value_counts()
)

print(bridge_analysis)

bridge_analysis.to_csv(
    "bridge_analysis.csv"
)


# =========================================================
# TUNNEL ANALYSIS
# =========================================================

print("\n=================================================")
print("TUNNEL ANALYSIS")
print("=================================================")

tunnel_analysis = (
    roads["tunnel"]
    .fillna("No")
    .value_counts()
)

print(tunnel_analysis)

tunnel_analysis.to_csv(
    "tunnel_analysis.csv"
)


# =========================================================
# TOP 20 LONGEST ROAD SEGMENTS
# =========================================================

print("\n=================================================")
print("TOP 20 LONGEST ROAD SEGMENTS")
print("=================================================")

longest_roads = (
    roads[
        ["name_cleaned", "highway_cleaned", "length"]
    ]
    .sort_values(
        by="length",
        ascending=False
    )
    .head(20)
)

print(longest_roads)

longest_roads.to_csv(
    "longest_roads.csv",
    index=False
)

# =========================================================
# MOST FREQUENT ROAD NAMES
# =========================================================

print("\n=================================================")
print("MOST FREQUENT ROAD NAMES")
print("=================================================")

top_names = (
    roads["name_cleaned"]
    .value_counts()
    .head(20)
)

print(top_names)

top_names.to_csv(
    "top_road_names.csv"
)

# =========================================================
# NETWORK SUMMARY
# =========================================================

print("\n=================================================")
print("ROAD NETWORK SUMMARY")
print("=================================================")

print(
    f"Total Road Segments: {len(roads):,}"
)

print(
    f"Average Road Length: {round(roads['length'].mean(),2)} m"
)

print(
    f"Maximum Road Length: {round(roads['length'].max(),2)} m"
)

print(
    f"Minimum Road Length: {round(roads['length'].min(),2)} m"
)

print("\nAnalysis completed successfully.")