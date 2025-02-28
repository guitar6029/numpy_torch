import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the CSV file into a DataFrame
df = pd.read_csv('music.csv')

# Step 2: Create a histogram using Seaborn
sns.histplot(df['Duration (s)'], bins=10, kde=True)  # Adjust the column name and parameters as needed

# Step 3: Display the plot
plt.show()
