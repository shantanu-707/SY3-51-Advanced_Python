import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")

print("First five records:")
print(df.head())
print("\nDataset information:")
df.info()

print("\nAverage marks:", df["Marks"].mean())
print("Maximum marks:", df["Marks"].max())
print("Minimum marks:", df["Marks"].min())

print("\nStudents scoring more than 75:")
print(df[df["Marks"] > 75])

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

axes[0].bar(df["Name"], df["Marks"], color="skyblue")
axes[0].set_title("Marks Obtained by Each Student")
axes[0].set_xlabel("Student")
axes[0].set_ylabel("Marks")
axes[0].tick_params(axis="x", rotation=45)

axes[1].hist(df["Marks"], bins=5, color="orange", edgecolor="black")
axes[1].set_title("Distribution of Marks")
axes[1].set_xlabel("Marks")
axes[1].set_ylabel("Number of Students")

axes[2].scatter(df["Study_Hours"], df["Marks"], color="green")
axes[2].set_title("Study Hours vs Marks")
axes[2].set_xlabel("Study Hours")
axes[2].set_ylabel("Marks")

plt.tight_layout()
plt.show()
