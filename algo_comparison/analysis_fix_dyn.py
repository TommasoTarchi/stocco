import pandas as pd



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_fix_dyn.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)


# Calculate means and standard deviations

mean_fs = df['fixed_simulation'].mean()
stddev_fs = df['fixed_simulation'].std()

mean_ds = df['dynamic_simulation'].mean()
stddev_ds = df['dynamic_simulation'].std()

mean_fe = df['fixed_elapsed'].mean()
stddev_fe = df['fixed_elapsed'].std()

mean_de = df['dynamic_elapsed'].mean()
stddev_de = df['dynamic_elapsed'].std()


# Print the results

print("fixed_simulation:")
print(f"Mean: {mean_fs}")
print(f"Standard Deviation: {stddev_fs}\n")

print("dynamic_simulation:")
print(f"Mean: {mean_ds}")
print(f"Standard Deviation: {stddev_ds}")

print()

print("fixed_elapsed:")
print(f"Mean: {mean_fe}")
print(f"Standard Deviation: {stddev_fe}\n")

print("dynamic_elapsed:")
print(f"Mean: {mean_de}")
print(f"Standard Deviation: {stddev_de}")
