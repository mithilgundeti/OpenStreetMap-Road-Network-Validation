import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

roads_path = project_root / "data" / "roads.csv"

roads = pd.read_csv(roads_path)

sample = roads.sample(
    n=5000,
    random_state=42
)

sample.to_csv(
    project_root / "data" / "roads_sample.csv",
    index=False
)

print("roads_sample.csv created successfully")