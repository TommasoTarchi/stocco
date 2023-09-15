import pandas as pd

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('flat.csv', comment='#')

# Calculate the mean and standard deviation of Column1
mean_column1 = df['exact_simulation'].mean()
stddev_column1 = df['exact_simulation'].std()

# Calculate the mean and standard deviation of Column2
mean_column2 = df['hybrid_simulation'].mean()
stddev_column2 = df['hybrid_simulation'].std()

# Print the results
print("Column1:")
print(f"Mean: {mean_column1}")
print(f"Standard Deviation: {stddev_column1}\n")

print("Column2:")
print(f"Mean: {mean_column2}")
print(f"Standard Deviation: {stddev_column2}")
