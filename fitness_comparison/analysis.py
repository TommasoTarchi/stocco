import pandas as pd



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)


# Calculate means and standard deviations

mean_flat = df['flat_simul'].mean()
stddev_flat = df['flat_simul'].std()

mean_static_inc = df['static_inc_simul'].mean()
stddev_static_inc = df['static_inc_simul'].std()

mean_static_dec = df['static_dec_simul'].mean()
stddev_static_dec = df['static_dec_simul'].std()

mean_static_mount = df['static_mount_simul'].mean()
stddev_static_mount = df['static_mount_simul'].std()

mean_dynamic = df['dynamic_simul'].mean()
stddev_dynamic = df['dynamic_simul'].std()


# Print the results

print("flat fitness:")
print(f"Mean: {mean_flat}")
print(f"Standard Deviation: {stddev_flat}\n")

print()

print("static increasing fitness:")
print(f"Mean: {mean_static_inc}")
print(f"Standard Deviation: {stddev_static_inc}\n")

print()

print("static decreasing fitness:")
print(f"Mean: {mean_static_dec}")
print(f"Standard Deviation: {stddev_static_dec}\n")

print()

print("static 'mountain' fitness:")
print(f"Mean: {mean_static_mount}")
print(f"Standard Deviation: {stddev_static_mount}\n")

print()

print("dynamic fitness:")
print(f"Mean: {mean_dynamic}")
print(f"Standard Deviation: {stddev_dynamic}\n")
