import pandas as pd
import matplotlib.pyplot as plt



# Read the data file into a DataFrame
data = pd.read_csv('data_const.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with fixed N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('const.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_log.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with log-increasing N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('log.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_1.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N_tilde, label='N_tilde', marker='o', linestyle='-')
plt.plot(time, N, label='N_1', marker='s', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_2.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N, label='N_2', marker='s', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_3.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N, label='N_3', marker='s', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_4.csv')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N, label='N_4', marker='s', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in spatial model with fixed N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('spatial.png')
