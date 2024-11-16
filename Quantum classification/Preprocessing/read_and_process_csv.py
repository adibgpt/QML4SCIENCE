# Import necessary libraries
import pandas as pd

# Read and process CSV
data = pd.read_csv("file.csv", usecols=[1, 2])
data['class'] = data['class_number'] == 1

# Display the first few rows and class distribution
print(data.head())
print(data['class'].value_counts())
