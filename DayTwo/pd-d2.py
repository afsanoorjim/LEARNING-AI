import pandas as pd
import numpy as np

import faker

data = pd.read_csv("results.csv")
fake = faker.Faker()
names = []
for _ in range(data.shape[0]):
    names.append(fake.name())

data["Name"] = names

data.to_csv("results2.csv", index=False)
df = pd.read_csv("results2.csv")


top_students = []
for num in df["Total"]:
    if num == df['Total'].max():
        top_students.append(df[df['Total'] == num]['Name'].values[0])
    elif num<df["Total"].max() and len(top_students) < 9:
        top_students.append(df[df['Total'] == num]['Name'].values[0])

print(top_students)
print(len(top_students))
print(df['Total'].max())

pd.to_csv(top_students, "top_students.csv", index=False)

