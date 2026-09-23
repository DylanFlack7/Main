import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(0)

n_pos = n_neg = 20

mean_moves = { 'Positive' : {'2Y' : +15, '10Y' : +6, 'S&P' : -0.7, 'USD' : +0.5},
              'Negative' : {'2Y' : -12, '10Y' : -5, 'S&P' : +0.6, 'USD' : -0.4}}

std_moves = {'2Y' : 5, '10Y' : 3, 'S&P' : 0.3, 'USD' : 0.2}

events = []
for s, count in [('Positive', n_pos), ('Negative', n_neg)]:
    for _ in range(count):
        events.append({'Surprise' : s, 
                        'd2Y_bps' : np.random.normal(mean_moves[s]['2Y'], std_moves['2Y']),
                        'd10Y_bps' : np.random.normal(mean_moves[s]['10Y'], std_moves['10Y']),
                        'dSP_pct' : np.random.normal(mean_moves[s]['S&P'], std_moves['S&P']),
                        'dUSD_pct' : np.random.normal(mean_moves[s]['USD'], std_moves['USD'])})

df = pd.DataFrame(events)
print(df)

avg_moves = df.groupby('Surprise').mean()
print(avg_moves)

labels = ['2Y Yield', '10Y Yield', 'S&P 500', 'USD Index']
pos = avg_moves.loc['Positive'].values
neg = avg_moves.loc['Negative'].values

x = np.arange(len(labels))
w = 0.35
plt.figure(figsize=(10, 5))

plt.bar(x - w/2, pos, w, label = 'Positive Surprise')
plt.bar(x + w/2, neg, w, label = 'Negative Surprise')

plt.axhline(0, color = 'black', linewidth = 0.8)
plt.xticks(x, labels)
plt.ylabel('Average Same-Day Change (bps / %)')
plt.title('Market Moves on CPI Surprise Days')
plt.legend()
plt.tight_layout()
plt.show()

plt.savefig('cpi_chart.png')