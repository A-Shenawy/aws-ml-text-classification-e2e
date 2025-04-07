import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import s3fs

# Load data
dataset = pd.read_csv('s3://shenawy-ml-text/IMDB Dataset.csv')
df = dataset.head(100)

# Perform EDA steps
print(df.head())  
print(df.info())  
print(df.describe())  
print(df.isnull().sum())

# Visualize the class distribution (sentiment column)
class_counts = df["sentiment"].value_counts()
print(class_counts)

# Plotting the class distribution
plt.figure(figsize=(8,6))
plt.bar(class_counts.index, class_counts.values)
plt.title("Class Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")

# Save the plot
plt.savefig("class_distribution.png") 