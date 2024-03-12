import pandas as pd
import matplotlib.pyplot as plt

surveys_df = pd.read_csv("surveys.csv")

print(surveys_df.head())
print("\nDataFrame columns:")
print(surveys_df.columns.to_list())
print("\nUnique species IDs:")
print(pd.unique(surveys_df["species_id"]))

print("\nWeight column statistics:")
print(surveys_df["weight"].describe())

surveys_df["weight"] = pd.to_numeric(surveys_df["weight"])

print("presiona arreglo")
select = int(input())

if select == 1:
    grouped_data = surveys_df.groupby(["weight"])
    print(grouped_data.describe())
else:
    print("me rompi")
