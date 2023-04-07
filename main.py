import pandas as pd
import os
from tqdm import tqdm

file_list = list()
df_list = list()
for root, dirs, files in os.walk('/home/user/Documents/Moloko'):
    for file in files:
        if file.endswith('.csv'):
            file_list.append(os.path.join(root, file))
for file in tqdm(file_list):
    df = pd.read_csv(file, index_col=[0])
    conc = float(file.split(os.sep)[-1].split("_")[1])
    antibiotic = file.split(os.sep)[-1].split("_")[0]
    values = list(df[df.columns[1]].values)
    values.append(antibiotic)
    values.append(conc)
    df_list.append(values)
    feature_n = list(df[df.columns[0]].values)
    feature_n.append('antibiotic')
    feature_n.append('concetration')
main_df = pd.DataFrame(data=df_list, columns=feature_n)
main_df.to_csv('result_milk.csv')
