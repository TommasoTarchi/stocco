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
