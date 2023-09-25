import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)
df = df.drop(columns=['simulation_time', 'elapsed_time', 'state_world'])
data = np.reshape(df.values, (int(df.values.shape[1]**(1/2)), int(df.values.shape[1]**(1/2))))

avgs = np.zeros(data.shape)

for i in range(data.shape[0]):

    for j in range(data.shape[1]):

        string_array = data[i, j].replace('          ', ',')
        string_array = string_array.replace('         ', ',')
        string_array = string_array.replace('        ', ',')
        string_array = string_array.replace('       ', ',')
        string_array = string_array.replace('      ', ',')
        string_array = string_array.replace('     ', ',')
        string_array = string_array.replace('    ', ',')
        string_array = string_array.replace('   ', ',')
        string_array = string_array.replace('  ', ',')
        string_array = string_array.replace(' ', ',')
        if string_array[1] == ',':
            string_array = string_array[0] + string_array[2:]
        
        proper_array = ast.literal_eval(string_array)
        
        for k in range(len(proper_array)):
            avgs[i, j] += k*proper_array[k]

        avgs[i, j] /= sum(proper_array)

norm = np.max(avgs)

avgs /= norm

plt.imshow(avgs, cmap='Blues', vmin=0, vmax=1)
#plt.colorbar()  # Add a colorbar for reference
plt.title("Average genotipic class on each area")
plt.savefig("genotipes.png")
