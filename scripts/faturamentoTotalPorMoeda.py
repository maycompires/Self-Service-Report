import pandas as pd

# Leia o arquivo excel usando a função fornecida
FILEPATH = 'Meganium_Sales_data.xlsx'
dataframes = read_all_sheets_from_excel(FILEPATH)

# Considere a planilha 'consolidate' do arquivo excel
consolidate_df = dataframes['consolidate']

# Agrupar por moeda e somar a coluna total_price
faturamento = consolidate_df.groupby('currency', as_index=False)['total_price'].sum()

print(faturamento)
print('done')