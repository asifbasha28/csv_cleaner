import pandas as pd

data = pd.read_csv("messy.csv")

data["name"] = data["name"].str.strip().str.title()
data["city"] = data["city"].str.strip().str.title()
data["city"] = data["city"].replace({"Hyd" : "Hyderabad"})
data = data.drop_duplicates()
data = data.reset_index(drop=True)
data.to_csv("clean.csv", index=False)