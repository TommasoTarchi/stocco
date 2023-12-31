import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Read the CSV file into a Pandas DataFrame
datafile = 'data.csv'
df = pd.read_csv(datafile, comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["flat_simul", "static_inc_simul", "static_mount_simul", "static_mount+dynamic_simul"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time with dynamic population and different fitness landscapes")

# Save the plot as a PNG file
plt.savefig("simul_time.png")


data = df[["flat_state", "static_inc_state", "static_dec_state", "static_mount_state", "static_mount+dynamic_state"]]

# Create a boxplot to compare the four quantities
plt.figure(figsize=(12, 6))  # Optional: Set the figure size

# Choose the row you want to plot (e.g., row 0)
row_index = 7   # "cherrypicked"

# Select the specific row based on the index
selected_row = data.iloc[row_index]

# defining class labels
fitness_names = ["flat_state", "static_inc_state", "static_dec_state", "static_mount_state", "static_mount+dynamic_state"]
fitness_labels = ["flat", "static increasing", "static decreasing", "static 'mountain'", "static 'mountain' + dynamic"]

# Create an array of class labels
classes = np.arange(4)

for i in range(len(fitness_labels)):

    freq = selected_row[fitness_names[i]].strip('[]')
    freq = freq.split()

    # Convert the values to a list of floats
    numeric_freq = [float(val) for val in freq][:4]

#    freq_dict = dict(zip(classes, numeric_freq))

    plt.subplot(2, 3, i+1)

    # Create a bar chart
    plt.bar(classes, numeric_freq, tick_label=classes.tolist())

    # Customize the plot (optional)
    plt.xlabel('genotipic class')
    plt.ylabel('population')
    plt.title(fitness_labels[i])
    plt.legend()


row_index = 2

datafile = 'data_dyndec.csv'
df = pd.read_csv(datafile, comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)
data = df[["dynamic_dec_state"]]

selected_row = data.iloc[row_index]
freq = selected_row["dynamic_dec_state"].strip('[]')
freq = freq.split()

numeric_freq = [float(val) for val in freq][:4]

plt.subplot(2, 3, 6)

plt.bar(classes, numeric_freq, tick_label=classes.tolist())

plt.xlabel('genotipic class')
plt.ylabel('population')
plt.title("static decreasing + dynamic")
plt.legend()


plt.tight_layout()

# Show the bar chart
plt.savefig("genotipes.png")
