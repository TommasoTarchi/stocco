import pandas as pd
import numpy as np



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_ngb.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)
df = df.drop(columns=['simulation_time', 'elapsed_time', 'state_world'])
data = df.values
colors = np.zeros(data.shape[0])

# Define colors for classes 1 to 4 (light to dark)
class_colors = ['#FFD700', '#FFA500', '#FF8C00', '#FF4500']  # Adjust colors as needed

for i in range(data.shape[0]):
    
    # Calculate the average color based on frequencies
    total_frequency = sum(data[i])
    average_color = [
        sum(data[i][j] / total_frequency * int(color[j:j+2], 16) for j in (1, 3, 5))  # RGB channels
        for color in class_colors
    ]

    # Convert the average color to hexadecimal format
    colors[i] = "#{:02X}{:02X}{:02X}".format(*average_color)
