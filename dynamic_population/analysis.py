import pandas as pd
import matplotlib.pyplot as plt



# Read the data file into a DataFrame
data = pd.read_csv('data_const.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N_tilde, label='N_tilde', linestyle='-')
plt.plot(time, N, label='N', linestyle='--')

# Set labels and title
plt.ylim(7000, 12000)
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with fixed N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('const.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_log.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

# Create a plot
plt.figure(figsize=(10, 6))
plt.plot(time, N_tilde, label='N_tilde', linestyle='-')
plt.plot(time, N, label='N', linestyle='--')

# Set labels and title
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in non spatial model with log-increasing N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('log.png')


# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_1.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

time_max = time.copy()
N_tilde_max = N_tilde.copy()

# Create a plot
plt.figure(figsize=(10, 6))

plt.plot(time, N, label='N_1', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_2.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

if time.shape[0] > time_max.shape[0]:
    time_max = time.copy()
    N_tilde_max = N_tilde.copy()

# Create a plot
plt.plot(time, N, label='N_2', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_3.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

if time.shape[0] > time_max.shape[0]:
    time_max = time.copy()
    N_tilde_max = N_tilde.copy()

# Create a plot
plt.plot(time, N, label='N_3', linestyle='--')

# Read the data file into a DataFrame
data = pd.read_csv('data_spatial_4.csv', comment='#')

# Extract columns
time = data['t']
N_tilde = data['N_tilde']
N = data['N']

if time.shape[0] > time_max.shape[0]:
    time_max = time.copy()
    N_tilde_max = N_tilde.copy()

# Create a plot
plt.plot(time, N, label='N_4', linestyle='--')

# plotting N_tilde
plt.plot(time_max, N_tilde_max, label='N_tilde', linestyle='-')

# Set labels and title
plt.ylim(7000, 12000)
plt.xlabel('simulation time')
plt.ylabel('population size')
plt.title('Population in spatial model with fixed N_tilde')
plt.legend()

# save plot as an image file
plt.savefig('spatial.png')
