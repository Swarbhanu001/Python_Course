import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option("display.width", 120) # sets how many characters wide the console output can be before pandas wraps a table onto multiple lines
pd.set_option("display.max_columns", 30) # sets how many columns pandas will actually show before it starts hiding the middle ones and printing ... instead

# 1. Read CSV file and transfer it into a DataFrame
# Note: by default pandas treats the text "None" as a missing value too,
# but in the AirBags column "None" is a real category (no airbags), not missing data.
# So we tell pandas to only treat "NA" (and blank cells) as missing, to avoid wrongly marking 32 valid "None" airbag entries as NaN.
try:
    df = pd.read_csv("Cars93_missing.csv", encoding="utf-8", keep_default_na=False, na_values=["NA", ""])
except FileNotFoundError:
    print("Error: Cars93_missing.csv not found in current directory")
    exit()
print(df.head())

# 2. Transfer an object Series into the index column of the DataFrame
df = df.set_index("Make")
print("2. Missing index labels:", df.index.isna().sum(), "(cars with no Make listed)\n")
print(df.head())
# 3. Change the data in the column of DataFrame according to some condition

df.loc[df["Horsepower"] > 200, "Horsepower"] = df.loc[df["Horsepower"] > 200, "Horsepower"].apply(lambda x: (x // 10) * 10)

# 4.Get names of the DataFrame columns and sum of lost values DF

print("4. Columns:", list(df.columns))
print("\n   Missing values per column:")
missing_counts = df.isnull().sum()
for col, count in missing_counts.items():
    print(f"   - {col}: {count}")
print("\n   Total missing values:", missing_counts.sum(), "\n")

# 5. Exchange 2 columns using a function; sort columns by name

def swap_columns(frame, col1, col2):
    """Return a copy of the DataFrame with the positions of col1 and col2 exchanged."""
    cols = list(frame.columns)
    i, j = cols.index(col1), cols.index(col2)
    cols[i], cols[j] = cols[j], cols[i]
    return frame[cols]


print("5. Before swap:", list(df.columns[:5]))
df = swap_columns(df, "Manufacturer", "Price")
print("   After swap: ", list(df.columns[:5]))

df_sorted = df.sort_index(axis=1)  # columns sorted alphabetically
print("   Sorted columns:", list(df_sorted.columns), "\n")

# 6. Delete the upper and lower 5% in the DataFrame

low = df["Price"].quantile(0.05)
high = df["Price"].quantile(0.95)
df_trimmed = df[(df["Price"] >= low) & (df["Price"] <= high)]
print(f"6. 5% quantile = {low}, 95% quantile = {high}")
print(f"   Rows before: {len(df)} | rows after: {len(df_trimmed)}")
print("   (rows with missing Price are dropped too, since they can't be compared)\n")

# 7. Replace (fill) missing values in a column with the average value

print("7. Luggage.room missing before:", df["Luggage.room"].isna().sum())
df["Luggage.room"] = df["Luggage.room"].fillna(df["Luggage.room"].mean())
print("   Luggage.room missing after: ", df["Luggage.room"].isna().sum())

# 8. Create two DataFrames from two dicts; merge them, and append the
#    second as a new column (or columns) to the first

dict1 = {"Car": ["Audi 90", "BMW 535i", "Ford Escort", "Honda Civic"],
         "Price": [29.1, 30.0, 10.1, 12.1]}
dict2 = {"Car": ["Audi 90", "BMW 535i", "Ford Escort", "Honda Civic"],
         "Horsepower": [172, 208, 127, 102]}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

merged = pd.merge(df1, df2, on="Car")
print("8. Merged DataFrame:")
print(merged, "\n")

appended = pd.concat([df1, df2.drop(columns="Car")], axis=1)
print("   Appended as new column(s):")
print(appended, "\n")

# 9. Create a histogram for a column

plt.figure(figsize=(7, 4))
df["Horsepower"].plot(kind="hist", bins=15, edgecolor="black")
plt.title("Distribution of horsepower")
plt.xlabel("Horsepower")
plt.ylabel("Number of cars")
plt.savefig("horsepower_histogram.png")
print("9. Saved horsepower_histogram.png")
plt.close()

# 10. Create a correlation matrix for any column

cols = ["Price", "MPG.city", "EngineSize", "Horsepower", "Weight", "Length", "Fuel.tank.capacity"]
corr = df[cols].corr()
print("Correlation matrix:")
print(corr.round(2), "\n")

plt.figure(figsize=(7, 6))
plt.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)
plt.xticks(range(len(cols)), cols, rotation=45, ha="right")
plt.yticks(range(len(cols)), cols)
plt.colorbar()
plt.title("Correlation matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png")
print("Saved correlation_matrix.png")
plt.close()