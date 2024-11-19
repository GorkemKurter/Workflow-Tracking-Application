import pandas as pd
import sqlite3

df_ELK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='ELK',skiprows=1,usecols='F:R')
df_filtered_ELK = df_ELK.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
df_filtered_ELK = df_filtered_ELK.rename(columns={
        df_filtered_ELK.columns[0] : 'Part_name',
        df_filtered_ELK.columns[1] : 'Manufacturer',
        df_filtered_ELK.columns[2] : 'Model',
        df_filtered_ELK.columns[3] : 'Technical_Data',
        df_filtered_ELK.columns[4] : 'Standard',
        df_filtered_ELK.columns[5] : 'Mark_of_Conformity',
        df_filtered_ELK.columns[6] : 'F_Washer_LVD',
        df_filtered_ELK.columns[7] : 'T_Washer_LVD',
        df_filtered_ELK.columns[8] : 'F_Washer_Dryer_LVD',
        df_filtered_ELK.columns[9] : 'T_Washer_Dryer_LVD'
})
conn = sqlite3.connect('ELK_renamed.db')
df_filtered_ELK.to_sql(name='ELK', con=conn, if_exists='replace', index=False)
conn.close()

df_EMK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='EMK',skiprows=1,usecols='F:R')
df_filtered_EMK = df_EMK.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
df_filtered_EMK = df_filtered_EMK.rename(columns={
        df_filtered_EMK.columns[0] : 'Part_name',
        df_filtered_EMK.columns[1] : 'Manufacturer',
        df_filtered_EMK.columns[2] : 'Model',
        df_filtered_EMK.columns[3] : 'Technical_Data',
        df_filtered_EMK.columns[4] : 'Standard',
        df_filtered_EMK.columns[5] : 'Mark_of_Conformity',
        df_filtered_EMK.columns[6] : 'F_Washer_LVD',
        df_filtered_EMK.columns[7] : 'T_Washer_LVD',
        df_filtered_EMK.columns[8] : 'F_Washer_Dryer_LVD',
        df_filtered_EMK.columns[9] : 'T_Washer_Dryer_LVD'
})
conn = sqlite3.connect('EMK_renamed.db')
df_filtered_EMK.to_sql(name='EMK', con=conn, if_exists='replace', index=False)
conn.close()

df_Control = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='Kontrol_G.',skiprows=2,usecols='G:S')
print(df_Control)
df_filtered_Control = df_Control.drop(columns=['Certificate Link', 'Parça Test Linki','Certificate Number'])
df_filtered_Control = df_filtered_Control.rename(columns={
        df_filtered_Control.columns[0] : 'Part_name',
        df_filtered_Control.columns[1] : 'Manufacturer',
        df_filtered_Control.columns[2] : 'Model',
        df_filtered_Control.columns[3] : 'Technical_Data',
        df_filtered_Control.columns[4] : 'Standard',
        df_filtered_Control.columns[5] : 'Mark_of_Conformity',
        df_filtered_Control.columns[6] : 'F_Washer_LVD',
        df_filtered_Control.columns[7] : 'T_Washer_LVD',
        df_filtered_Control.columns[8] : 'F_Washer_Dryer_LVD',
        df_filtered_Control.columns[9] : 'T_Washer_Dryer_LVD'
})
conn = sqlite3.connect('Control_renamed.db')
df_filtered_Control.to_sql(name='Control', con=conn, if_exists='replace', index=False)
conn.close()