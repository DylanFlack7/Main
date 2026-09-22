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
