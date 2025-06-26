# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# load the csv file
df = pd.read_csv("employees.csv")

# inspect the initial df
print(f"Initial dataset:\n {df}")

# data cleaning
# fill the missing salary for Eve with the avg salary
avg_salary_hr = df[df["department"] == "HR"]["salary"].mean()
df.loc[(df["department"] == "HR") & (df["salary"].isna()), "salary"] = avg_salary_hr

# data transformation - avg salary per department
avg_salaries_per_dep = df.groupby("department")["salary"].mean().reset_index()

# display the avg salary per department
print("\nAverage salary per departemnt: ")
print(avg_salaries_per_dep)

# export the cleaned data and the summary to a new csv
df.to_csv("employees_cleaned.csv", index=False)
avg_salaries_per_dep.to_csv("average_salary.csv", index=False)


# visualizing the data with matplotlib

# set figure size for better clarity
plt.figure(figsize=(8, 6))

# create a bar chart
plt.bar(
    avg_salaries_per_dep["department"], avg_salaries_per_dep["salary"], color="skyblue"
)

# add label and title
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Average Salary per Department")
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.savefig("average_salary_chart.png", dpi=300)

# display the plot
plt.show()

# Salary distribution
plt.figure(figsize=(8, 6))
sns.histplot(df["salary"], bins=10, kde=True)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.savefig("salary_distribution", dpi=300)

plt.show()

# Salary distribution by department (boxplot)
plt.figure(figsize=(8, 6))
sns.boxplot(x="department", y="salary", data=df)
plt.title("Salary Distribution by Department")

plt.savefig("salary_distribution_by_depart", dpi=300)

plt.show()
