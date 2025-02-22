import pandas as pd

# Group by country and product, count occurrences
popular_by_country = consolidate_df.groupby(['delivery_country', 'product_sold'])['quantity'].sum().reset_index()

# Sort within each country to get the most popular product
most_popular = popular_by_country.sort_values(['delivery_country', 'quantity'], ascending=[True, False])

# Get the top product for each country
top_products = most_popular.groupby('delivery_country').head(1).sort_values('quantity', ascending=False)

print("Produtos mais populares por país (ordenado por quantidade):")
print(top_products)