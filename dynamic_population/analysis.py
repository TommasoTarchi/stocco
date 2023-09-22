import pandas as pd
import matplotlib.pyplot as plt



# Read the data file into a DataFrame
data = pd.read_csv('data_const.csv')

# Extract the time, quantity1, and quantity2 columns
time = data['t']  # Replace 'Time' with the actual column name for time
N_tilde = data['N_tilde']  # Replace 'Quantity1' with the actual column name for quantity 1
N = data['N']  # Replace 'Quantity2' with the actual column name for quantity 2

# Create a plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with fixed N_tilde')
plt.legend()

# Show the plot or save it as an image file
plt.savefig('const.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_log.csv')

# Extract the time, quantity1, and quantity2 columns
time = data['t']  # Replace 'Time' with the actual column name for time
N_tilde = data['N_tilde']  # Replace 'Quantity1' with the actual column name for quantity 1
N = data['N']  # Replace 'Quantity2' with the actual column name for quantity 2

# Create a plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with log-increasing N_tilde')
plt.legend()

# Show the plot or save it as an image file
plt.savefig('log.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_spatial.csv')

# Extract the time, quantity1, and quantity2 columns
time = data['t']  # Replace 'Time' with the actual column name for time
N_tilde = data['N_tilde']  # Replace 'Quantity1' with the actual column name for quantity 1
N = data['N']  # Replace 'Quantity2' with the actual column name for quantity 2

# Create a plot
plt.figure(figsize=(10, 6))  # Optional: Set the figure size
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in spatial model with fixed N_tilde')
plt.legend()

# Show the plot or save it as an image file
plt.savefig('spatial.png')
