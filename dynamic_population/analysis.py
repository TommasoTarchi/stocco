import pandas as pd
import matplotlib.pyplot as plt

# Read the data file into a DataFrame
data = pd.read_csv('data_const.csv')  # Replace 'your_data_file.csv' with the actual file path

# Extract the time, quantity1, and quantity2 columns
time = data['simulation time']  # Replace 'Time' with the actual column name for time
quantity1 = data['']  # Replace 'Quantity1' with the actual column name for quantity 1
quantity2 = data['2']  # Replace 'Quantity2' with the actual column name for quantity 2

# Create a plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(time, quantity1, label='Quantity 1', marker='o', linestyle='-')
plt.plot(time, quantity2, label='Quantity 2', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Plot of Quantity 1 and Quantity 2 Over Time')
plt.legend()

# Show the plot or save it as an image file
plt.show()
# To save the plot as an image file (e.g., PNG), use plt.savefig('output.png')
