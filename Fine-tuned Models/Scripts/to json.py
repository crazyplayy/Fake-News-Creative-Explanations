import pandas as pd

csv = pd.read_csv('to_transform_json2.csv', sep=';')

csv.to_json("gpt-3-humor-db.jsonl", orient='records', lines=True)