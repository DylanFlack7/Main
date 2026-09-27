import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cpi = pd.read_csv('cpi_releases.csv')

cpi['surprise'] = cpi['actual'] - cpi['forecast']

url_2y = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS2'
yield_2y = pd.read_csv(url_2y)

url_10y = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10'
yield_10y = pd.read_csv(url_10y)

url_sp = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=SP500'
sp = pd.read_csv(url_sp)

url_usd = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=DTWEXBGS'
usd = pd.read_csv(url_usd)

markets = yield_2y.merge(yield_10y, on='observation_date')
markets = markets.merge(sp, on='observation_date')
markets = markets.merge(usd, on='observation_date')
markets = markets.dropna()

markets['d2Y_bps'] = markets['DGS2'].diff()*100
markets['d10Y_bps'] = markets['DGS10'].diff()*100
markets['dSP_pct'] = markets['SP500'].pct_change()*100
markets['dUSD_pct'] = markets['DTWEXBGS'].pct_change()*100

events = cpi.merge(markets, left_on='release_date', right_on='observation_date')

events['group'] = np.where(events['surprise'] > 0, 'Positive',
                  np.where(events['surprise'] < 0, 'Negative', 'In line'))

move_cols = ['d2Y_bps', 'd10Y_bps', 'dSP_pct', 'dUSD_pct']
avg_moves = events.groupby('group')[move_cols].mean()

labels = ['2Y Yield', '10Y Yield', 'S&P 500', 'USD Index']
pos = avg_moves.loc['Positive'].values
inl = avg_moves.loc['In line'].values
neg = avg_moves.loc['Negative'].values

x = np.arange(len(labels))
w = 0.25
plt.figure(figsize=(10, 5))

plt.bar(x - w/2, pos, w, label = 'Positive Surprise')
plt.bar(x, inl, w, label = 'In line')
plt.bar(x + w/2, neg, w, label = 'Negative Surprise')

plt.axhline(0, color = 'black', linewidth = 0.8)
plt.xticks(x, labels)
plt.ylabel('Average Same-Day Change (bps / %)')
plt.title('Market Moves on CPI Surprise Days')
plt.legend()
plt.tight_layout()
plt.show()

plt.savefig('cpi_chart_real.png')