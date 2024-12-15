import pandas as pd

# Soal No.1 Membuat DataFrame dari data jumlah produksi sampah berdasarkan Kabupaten/Kota di Jawa Barat
df_excel = pd.read_excel('Data1.xlsx')  
df_excel = df_excel[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']]
print("\nJUMLAH PRODUKSI SAMPAH BERDASARKAN KABUPATEN/KOTA DI JAWA BARAT:")
print(df_excel)


# Soal No.2 hitunglah total produksi sampah di seluruh Kabupaten/Kota di Jawa Barat untuk tahun tertentu.
total_sampah = 0
df_excel['jumlah_produksi_sampah'] = df_excel['jumlah_produksi_sampah'].fillna(0)
tahun_input = int(input("Masukkan tahun yang ingin dihitung total produksinya: "))
for index, row in df_excel.iterrows():
    if row['tahun'] == tahun_input:  
        total_sampah += row['jumlah_produksi_sampah']
print(f"\nTotal produksi sampah di seluruh Kabupaten/Kota pada tahun {tahun_input}: {total_sampah:.2f} ton")

# Soal No.3 Jumlahkan Data Pertahun
data_per_tahun = {}
for index, row in df_excel.iterrows():
    tahun = row['tahun']
    produksi = row['jumlah_produksi_sampah']
    data_per_tahun[tahun] = data_per_tahun.get(tahun, 0) + produksi
print("\nJumlah produksi sampah per tahun:")
for tahun, total in data_per_tahun.items():
    print(f"\n{tahun}: {total:.2f}")

# Soal No.4 Jumlahkan data per Kota/Kabupaten per tahun
data_per_kota_per_tahun = {}
for data, row in df_excel.iterrows():
    kota = row['nama_kabupaten_kota']
    tahun = row['tahun']
    produksi = row['jumlah_produksi_sampah'] 
    key = (kota, tahun)
    data_per_kota_per_tahun[key] = produksi

print("\nJumlah produksi sampah per Kota/Kabupaten per tahun:")
for key, total in data_per_kota_per_tahun.items():
    print(f"{key}: {total}\n")

df_excel.to_csv('Data1.csv', index=False)
df_excel

df_excel = pd.read_excel('Data1.xlsx', sheet_name=None)  
print(df_excel)  
