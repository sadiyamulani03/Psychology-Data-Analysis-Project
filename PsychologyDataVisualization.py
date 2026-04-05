import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
#  DATA (NO CSV NEEDED)
# ==========================================
data = {
    "Year":   [2020, 2020, 2020, 2021, 2021, 2021, 2022, 2022, 2022],
    "Subject": ["Cognitive Psychology", "Abnormal Psychology", "Research Methods",
                "Cognitive Psychology", "Abnormal Psychology", "Research Methods",
                "Cognitive Psychology", "Abnormal Psychology", "Research Methods"],
    "Pass_Percent": [78, 72, 81, 80, 75, 85, 82, 78, 88],
    "Passed":       [156, 144, 162, 160, 150, 170, 164, 156, 176],
    "Failed":       [44, 56, 38, 40, 50, 30, 36, 44, 24]
}

df = pd.DataFrame(data)

print("\n------ DATA SAMPLE ------\n")
print(df.head())

# ==========================================
# 1. BAR CHART – Pass Percent
# ==========================================
plt.figure(figsize=(10,6))
sns.barplot(data=df, x='Year', y='Pass_Percent')
plt.title("SPPU Psychology - Pass Percentage (Bar Chart)")
plt.ylabel("Pass Percentage")
plt.savefig("bar_chart.png")
plt.show()

# ==========================================
# 2. LINE CHART – Total Pass Trend
# ==========================================
yearly_pass = df.groupby('Year')['Passed'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=yearly_pass, x='Year', y='Passed', marker='o')
plt.title("Passed Students Trend (Line Chart)")
plt.xlabel("Year")
plt.ylabel("Total Passed")
plt.savefig("line_chart.png")
plt.show()

# ==========================================
# 3. HISTOGRAM – Pass %
# ==========================================
plt.figure(figsize=(10,6))
sns.histplot(df['Pass_Percent'], bins=5)
plt.title("Distribution of Pass Percentage (Histogram)")
plt.xlabel("Pass %")
plt.savefig("histogram.png")
plt.show()

# ==========================================
# 4. PIE CHART – Passed vs Failed
# ==========================================
total_passed = df['Passed'].sum()
total_failed = df['Failed'].sum()

plt.figure(figsize=(6,6))
plt.pie([total_passed, total_failed],
        labels=['Passed', 'Failed'],
        autopct='%1.1f%%')
plt.title("Overall Result Distribution")
plt.savefig("pie_chart.png")
plt.show()

# ==========================================
# 5. HEATMAP – Subject-wise Pass Percent
# ==========================================
pivot = df.pivot_table(values='Pass_Percent', index='Year', columns='Subject')

plt.figure(figsize=(8,6))
sns.heatmap(pivot, annot=True, cmap="coolwarm")
plt.title("Pass Percentage Heatmap")
plt.savefig("heatmap.png")
plt.show()

# ==========================================
# 6. BOX PLOT – Subject-wise Distribution
# ==========================================
plt.figure(figsize=(8,6))
sns.boxplot(x='Subject', y='Pass_Percent', data=df)
plt.title("Boxplot of Pass Percent by Subject")
plt.savefig("boxplot.png")
plt.show()

print("\n✅ All charts successfully generated!")
