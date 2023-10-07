import pandas as pd

# Load your dataset
df = pd.read_csv("C:/Users/Personal/Downloads/Dataset (1).csv")  # Replace 'your_dataset.csv' with your dataset file path

# Count cuisines
Cuisine_counts = df['Cuisines'].value_counts()

# Select the top three cuisines
top_Cuisines = Cuisine_counts.head(3)

# Calculate percentages
total_restaurants = len(df)
percentage_top_cuisines = (top_Cuisines / total_restaurants) * 100

print("Top Three Cuisines:")
print(top_Cuisines)
print("\nPercentage of Restaurants Serving Each Top Cuisine:")
print(percentage_top_cuisines)
