import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Read the CSV file into a Pandas DataFrame
datafile = 'data_m4.csv'
df = pd.read_csv(datafile, comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)


# Create a boxplot to compare the four quantities
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

# Use the boxplot() method on the DataFrame
df.boxplot(column=["flat_simul", "static_inc_simul", "static_mount_simul", "dynamic_simul"])

# Set labels and title
#plt.xlabel("")
plt.ylabel("simulation time")
plt.title("Simulation time with dynamic population and different fitness landscapes")

# Save the plot as a PNG file
plt.savefig("simul_time.png")


data = df[["flat_state", "static_inc_state", "static_dec_state", "static_munt_state", "dynamic_state"]]

# Choose the row you want to plot (e.g., row 0)
row_index = 0   # "cherrypicked"

# Select the specific row based on the index
selected_row = data.iloc[row_index]

# defining class labels
class_labels = ["flat", "static increasing", "static decreasing", "static 'mountain'", "static 'mountain' + dynamic"]

# Extract counts for each class
class_counts = selected_row.values[:]  # Exclude the first column

# Create histograms for each class
plt.figure(figsize=(10, 6))  # Optional: Set the figure size

for i, class_label in enumerate(class_labels):
    # Convert the counts to a list of values for the current class
    class_data = [i + 1] * int(class_counts[i])  # Repeat class label based on count

    # Create a histogram for the current class
    plt.hist(
        class_data,
        bins=np.arange(0.5, len(class_labels) + 1.5),  # Create bins for each class
        alpha=0.5,
        label=class_label
    )

# Set labels and title
plt.xlabel('genotipic space')
plt.ylabel('population')
plt.title('Final state with fixed population and different fitness landscapes')

# Add class labels to the x-axis
plt.xticks(range(1, len(class_labels) + 1), class_labels)

# Add a legend
plt.legend()

# save plot as an image file
plt.savefig('final_states.png')
