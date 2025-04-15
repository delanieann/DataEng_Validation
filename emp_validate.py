import pandas as pd

data = pd.read_csv("employees.csv")

row_count = 0

for employee in data["name"]:
    if employee is None or pd.isna(employee):
        row_count += 1

print(f"First name assertion count: {row_count}")
