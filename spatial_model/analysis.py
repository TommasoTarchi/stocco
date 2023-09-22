import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('data_ngb.csv', comment='#', skip_blank_lines=True).dropna(axis=0).reset_index(drop=True)
df = df.drop(columns=['simulation_time', 'elapsed_time', 'state_world'])


selected_row = df.iloc[1]
