import pandas as pd

file = pd.read_csv('data_war_2022.csv')

print(file.columns)

selected_cols = file[['date', 'truth_o_meter','statement', 'tags', 'url']]

final_df = selected_cols[selected_cols['tags'].str.contains("Ukraine|Russia") == True]

final_df.to_csv('war.csv', encoding='utf-8')




#pd.set_option('display.max_colwidth', None)
#print(selected_cols[['Coronavirus' in x or 'Global Warming' in x for x in selected_cols['tags']]])
#print(selected_cols)