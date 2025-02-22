import pandas as pd

# Converter moedas para USD para comparação justa (usando taxas de conversão aproximadas)
conversion_rates = {
    'EUR': 1.1,  # EUR to USD
    'GBP': 1.27, # GBP to USD
    'USD': 1.0   # USD to USD (base)
}

# Criar uma nova coluna com preços convertidos
consolidate_df['price_usd'] = consolidate_df.apply(lambda row: row['total_price'] * conversion_rates[row['currency']], axis=1)

# Agrupar por produto e somar os preços convertidos
product_revenue = consolidate_df.groupby('product_sold')['price_usd'].sum().sort_values(ascending=False)

print("Produto mais lucrativo e seu faturamento (em USD):")
print(product_revenue.head(1))