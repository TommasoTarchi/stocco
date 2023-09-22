import pandas as pd
import matplotlib.pyplot as plt



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_spatial.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)



# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["base_elpsd", "4_elpsd"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("time(s)")
plt.title("Efficiency fixed Vs dynamic population algorithm")

# Save the plot as a PNG file
plt.savefig("eff_fix_dyn.png")
