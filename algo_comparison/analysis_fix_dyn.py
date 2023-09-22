import pandas as pd
import matplotlib.pyplot as plt



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_fix_dyn.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)



# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["fixed_elapsed", "dynamic_elapsed"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("time(s)")
plt.title("Efficiency fixed Vs dynamic population algorithm")

# Save the plot as a PNG file
plt.savefig("eff_fix_dyn.png")


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["fixed_simulation", "dynamic_simulation"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time fixed Vs dynamic population algorithm")

# Save the plot as a PNG file
plt.savefig("simul_fix_dyn.png")



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
