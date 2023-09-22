import pandas as pd
import matplotlib.pyplot as plt



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_fix_dyn.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)



# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))

# Use the boxplot() method on the DataFrame
df.boxplot(column=["fixed_elapsed", "dynamic_elapsed"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("time(s)")
plt.title("Efficiency fixed Vs dynamic population algorithm")

# Save the plot as a PNG file
plt.savefig("eff_fix_dyn.png")


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))

# Use the boxplot() method on the DataFrame
df.boxplot(column=["fixed_simulation", "dynamic_simulation"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time fixed Vs dynamic population algorithm")

# Save the plot as a PNG file
plt.savefig("simul_fix_dyn.png")
