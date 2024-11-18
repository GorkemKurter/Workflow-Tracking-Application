import pandas as pd
import sqlite3

'''df_ELK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='ELK',skiprows=1,usecols='F:R')
df_filtered_ELK = df_ELK.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
conn = sqlite3.connect('ELK.db')
df_filtered_ELK.to_sql(name='ELK', con=conn, if_exists='replace', index=False)
conn.close()
'''
<<<<<<< HEAD
'''df_EMK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='EMK',skiprows=1,usecols='F:R')
df_filtered_EMK = df_EMK.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
conn = sqlite3.connect('EMK.db')
df_filtered_EMK.to_sql(name='EMK', con=conn, if_exists='replace', index=False)
conn.close()'''

df_Control = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='Kontrol_G.',skiprows=2,usecols='G:S')
print(df_Control)
df_filtered_Control = df_Control.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
conn = sqlite3.connect('Control.db')
df_filtered_Control.to_sql(name='Control', con=conn, if_exists='replace', index=False)
=======
df_EMK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='EMK',skiprows=1,usecols='F:R')
df_filtered_EMK = df_EMK.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
conn = sqlite3.connect('EMK.db')
df_filtered_EMK.to_sql(name='EMK', con=conn, if_exists='replace', index=False)
>>>>>>> 40bd26ac11cadaa930eaa09a3f81ca24fe9019e2
conn.close()