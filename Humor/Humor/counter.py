import pandas as pd
from csv import writer

csv = pd.read_csv('HumorDB-Quatrains.csv', sep=';')
print(csv)

def summary_length(summary):
    summary = str(summary)
    return len(summary)

            
csv["Context Length"] = csv.apply(lambda row: summary_length(row["Column1"]), axis=1)
csv["Poem Length"] = csv.apply(lambda row: summary_length(row["Column2"]), axis=1)

csv.to_csv('counter-QuatrainsDB.csv', encoding='utf-8')

print('donezo')