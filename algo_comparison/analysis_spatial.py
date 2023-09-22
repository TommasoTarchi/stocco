import pandas as pd
import matplotlib.pyplot as plt



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_spatial.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)



# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))

# Use the boxplot() method on the DataFrame
df.boxplot(column=["base_elpsd", "4_elpsd", "16_elpsd", "36_elpsd", "64_elpsd"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("time(s)")
plt.title("Efficiency spatial algorithm with different resolutions")

# Save the plot as a PNG file
plt.savefig("eff_spatial.png")


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))

# Use the boxplot() method on the DataFrame
df.boxplot(column=["base_simul", "4_simul", "16_simul", "36_simul", "64_simul"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time spatial algorithm with different resolutions")

# Save the plot as a PNG file
plt.savefig("simul_spatial.png")
