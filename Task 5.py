# ================================
# LEVEL 2 - TASK 2
# Price Range Analysis
# ================================

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Dataset.csv")

# -------------------------------
# 1. Most common price range
# -------------------------------

price_counts = df['Price range'].value_counts()

print("\nMost Common Price Range:")
print(price_counts)

most_common_price = price_counts.idxmax()
print("\nMost Frequent Price Range:", most_common_price)

# -------------------------------
# 2. Average rating for each price range
# -------------------------------

avg_rating_price = df.groupby('Price range')['Aggregate rating'].mean()

print("\nAverage Rating for Each Price Range:")
print(avg_rating_price)

# -------------------------------
# 3. Which color has highest rating
# -------------------------------

# Some datasets have 'Rating color'
if 'Rating color' in df.columns:
    color_rating = df.groupby('Rating color')['Aggregate rating'].mean()

    print("\nAverage Rating by Color:")
    print(color_rating)

    highest_color = color_rating.idxmax()
    print("\nColor with Highest Average Rating:", highest_color)
else:
    print("\n'Rating color' column not found in dataset")

# -------------------------------
# 4. Visualization
# -------------------------------

# Price range distribution
price_counts.plot(kind='bar')
plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.show()

# Average rating per price range
avg_rating_price.plot(kind='bar', color='green')
plt.title("Average Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.show()