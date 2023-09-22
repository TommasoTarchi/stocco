import pandas as pd
import matplotlib.pyplot as plt



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_ex_hyb.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)



# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["exact_elapsed", "hybrid_elapsed"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("time(s)")
plt.title("Efficiency exact Vs hybrid algorithm")

# Save the plot as a PNG file
plt.savefig("eff_ex_hyb.png")


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["exact_simulation", "hybrid_simulation"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time exact Vs hybrid algorithm")

# Save the plot as a PNG file
plt.savefig("simul_ex_hyb.png")



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
