
import pandas as pd

# Load the CSV file
df = pd.read_csv('your_file.csv')

# Filter rows where column 'A' contains 'Ashwani'
filtered_df = df[df['A'] == 'Ashwani']

# Display the filtered data
print(filtered_df)
