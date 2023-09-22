import matplotlib.pyplot as plt
import numpy as np

# Sample array containing class frequencies
class_frequencies = [10, 20, 30, 40]

# Create an array of class labels
class_labels = np.arange(len(class_frequencies))  # [0, 1, 2, 3]

# Create a bar chart
plt.bar(class_labels, class_frequencies)

# Customize the plot (optional)
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.title('Histogram of Class Frequencies')

# Show the bar chart
plt.show()

