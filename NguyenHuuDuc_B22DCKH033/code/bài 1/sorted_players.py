import pandas as pd

df_players = pd.read_csv('results.csv', header=[0, 1])
first_row = df_players.iloc[0:1].copy()
df_data = df_players.iloc[1:].copy()
df_data.loc[:, ('Unnamed: 4_level_0', 'Unnamed: 4_level_1')] = (
    pd.to_numeric(df_data[('Unnamed: 4_level_0', 'Unnamed: 4_level_1')], errors='coerce'))
df_data = df_data.sort_values(
    by=[('Unnamed: 0_level_0', 'Unnamed: 0_level_1'), ('Unnamed: 4_level_0', 'Unnamed: 4_level_1')],
    ascending=[True, True],
    na_position='last' 
)
df_data.reset_index(drop=True, inplace=True)
df_sorted = pd.concat([first_row, df_data], ignore_index=True)
df_sorted.to_csv('results.csv', index=False, na_rep='N/A')
print(df_sorted)