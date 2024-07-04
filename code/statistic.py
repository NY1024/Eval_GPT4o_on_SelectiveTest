import pandas as pd

# Read the CSV file
df = pd.read_csv('2023_all.csv')

# Count the number of times the third column is equal to the fourth column
third_equals_fourth = (df.iloc[:, 2] == df.iloc[:, 3]).sum()

# Count the number of times the fourth column is equal to the sixth column
fourth_equals_sixth = (df.iloc[:, 3] == df.iloc[:, 5]).sum()

print(f"Number of times the third column equals the fourth column: {third_equals_fourth}")
print(f"Number of times the fourth column equals the sixth column: {fourth_equals_sixth}")
