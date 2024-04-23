import pandas as pd

dados = {
    'Real Madrid': 34,
    'Barcelona': 26,
    'juventus': 12,
    'Bayer Munich': 20
}

series_times = pd.Series(dados)
print(series_times.iloc[2])
print('\n')
print(series_times['Real Madrid':'Bayer Munich'])
print('\n')
print(series_times[series_times >= 26])