import pandas as pd
cpi = pd.read_csv('cpi_releases.csv')

cpi['surprise'] = cpi['actual'] - cpi['forecast']

print(cpi)