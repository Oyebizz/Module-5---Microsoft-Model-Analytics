# 5.1: Distribution of 'addedToCart'
from matplotlib import pyplot as plt
from xgboost import data
import seaborn as sns


plt.figure(figsize=(10, 6))
sns.histplot(data['addedToCart'], bins=30, kde=True, color='blue')
plt.title('Distribution of Added to Cart')
plt.xlabel('Added to Cart')
plt.ylabel('Frequency')
plt.show()

# 5.2: Purchase Distribution by Device Category
plt.figure(figsize=(12, 6))
sns.boxplot(x='deviceCategory', y='addedToCart', data=data)
plt.title('Added to Cart by Device Category')
plt.xlabel('Device Category')
plt.ylabel('Added to Cart (Standardized)')
plt.show()

# 5.3: Correlation Heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Features')
plt.show()

# 5.4: Purchase vs. Traffic Source
plt.figure(figsize=(12, 6))
sns.barplot(x='trafficSource', y='addedToCart', data=data, ci=None)
plt.title('Added to Cart by Traffic Source')
plt.xlabel('Traffic Source')
plt.ylabel('Added to Cart (Standardized)')
plt.xticks(rotation=45)
plt.show()
