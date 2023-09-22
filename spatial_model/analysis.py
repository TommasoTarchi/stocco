import pandas as pd
import numpy as np



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_ngb.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)
df = df.drop(columns=['simulation_time', 'elapsed_time', 'state_world'])
data = np.reshape(df.values, (int(df.values.shape[1]**(1/2)), int(df.values.shape[1]**(1/2))))

print(data)

avgs = np.zeros(data.shape)

for i in range(data.shape[0]):

    for j in range(data.shape[1]):

        freq = data[i, j][:4].strip('[]')
        freq = freq.split()

        numeric_freq = [float(val) for val in freq]

        avgs[i, j] = sum(numeric_freq)

print(avgs)
