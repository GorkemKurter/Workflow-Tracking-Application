import pandas as pd
import sqlite3
from datetime import date
'''df_ELK = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='ELK',skiprows=1,usecols='F:R')
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
conn.close()'''

'''import sqlite3
from datetime import date

# İlk veritabanına (EMK tablosunun bulunduğu) bağlan
conn_emk = sqlite3.connect('Control_renamed.db')  # İlk veritabanı dosyasının adını buraya yaz
cursor_emk = conn_emk.cursor()

# İkinci veritabanına (LVD_Management_System_component tablosunun bulunduğu) bağlan
conn_lvd = sqlite3.connect(r'WorkFlowTrackingTool//db.sqlite3')  # İkinci veritabanı dosyasının adını buraya yaz
cursor_lvd = conn_lvd.cursor()

# EMK tablosundan tüm verileri alıyoruz
cursor_emk.execute('SELECT * FROM Control')
emk_data = cursor_emk.fetchall()

# Tarih ve diğer varsayılan verileri ayarlıyoruz
default_date = '1999-11-11'
default_test_link = '-'
default_sap_code = '0'

# EMK tablosundan aldığımız verileri LVD_Management_System_component tablosuna ekliyoruz
for row in emk_data:
    part_name = row[0]
    manufacturer = row[1]
    model = row[2]
    technical_data = row[3]
    standard = row[4]
    mark_of_conformity = row[5]

    # F_Washer_LVD, T_Washer_LVD, F_Washer_Dryer_LVD ve T_Washer_Dryer_LVD alanları OK, NOK, eklenecek kontrolleri
    f_washer_lvd = 1 if row[6] in ['OK', 'eklenecek'] else 0
    t_washer_lvd = 1 if row[7] in ['OK', 'eklenecek'] else 0
    f_washer_dryer_lvd = 1 if row[8] in ['OK', 'eklenecek'] else 0
    t_washer_dryer_lvd = 1 if row[9] in ['OK', 'eklenecek'] else 0
    n_washer_lvd = 0  # N_Washer_LVD varsayılan olarak False (0)

    # LVD_Management_System_component tablosuna veriyi ekliyoruz
    cursor_lvd.execute('
        INSERT INTO LVD_Management_System_component (
            Part_name, 
            Manufacturer, 
            Model, 
            Technical_Data, 
            Standard, 
            Mark_of_Conformity, 
            F_Washer_LVD, 
            T_Washer_LVD, 
            F_Washer_Dryer_LVD, 
            T_Washer_Dryer_LVD, 
            N_Washer_LVD, 
            SAP_code, 
            Certificate_Expiry_Date, 
            Test_Results_Link, 
            Created_Date, 
            Last_Update_Date
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ', (
        part_name,
        manufacturer,
        model,
        technical_data,
        standard,
        mark_of_conformity,
        f_washer_lvd,
        t_washer_lvd,
        f_washer_dryer_lvd,
        t_washer_dryer_lvd,
        n_washer_lvd,
        default_sap_code,          # SAP_code varsayılan "0"
        default_date,              # Certificate_Expiry_Date varsayılan "1999-11-11"
        default_test_link,         # Test_Results_Link varsayılan "-"
        default_date,              # Created_Date varsayılan "1999-11-11"
        default_date               # Last_Update_Date varsayılan "1999-11-11"
    ))

# Değişiklikleri kaydet ve veritabanı bağlantılarını kapat
conn_lvd.commit()
conn_emk.close()
conn_lvd.close()

print("Veriler başarıyla aktarıldı.")'''

#df_Control = pd.read_excel(io='ComponentsParts_MasterList-v16_01.11.2023.xlsx',sheet_name='Kontrol_G.',skiprows=2,usecols='G:S')

account_df = pd.read_excel(io='Plansız&Faturalar_listesi.xlsx',sheet_name='Açılan Plansızlar',skiprows=1,usecols='C:M')
conn = sqlite3.connect('Account.db')
account_df.to_sql(name='Accounts', con=conn, if_exists='replace', index=False)
conn.close()