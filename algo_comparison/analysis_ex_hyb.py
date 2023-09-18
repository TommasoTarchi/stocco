import pandas as pd



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_ex_hyb.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)


# Calculate means and standard deviations

mean_es = df['exact_simulation'].mean()
stddev_es = df['exact_simulation'].std()

mean_hs = df['hybrid_simulation'].mean()
stddev_hs = df['hybrid_simulation'].std()

mean_ee = df['exact_elapsed'].mean()
stddev_ee = df['exact_elapsed'].std()

mean_he = df['hybrid_elapsed'].mean()
stddev_he = df['hybrid_elapsed'].std()


# Print the results

print("exact_simulation:")
print(f"Mean: {mean_es}")
print(f"Standard Deviation: {stddev_es}\n")

print("hybrid_simulation:")
print(f"Mean: {mean_hs}")
print(f"Standard Deviation: {stddev_hs}")

print()

print("exact_elapsed:")
print(f"Mean: {mean_ee}")
print(f"Standard Deviation: {stddev_ee}\n")

print("hybrid_elapsed:")
print(f"Mean: {mean_he}")
print(f"Standard Deviation: {stddev_he}")
