import pandas as pd
import numpy as np

# Membaca dataset dari file CSV
df_train = pd.read_csv('C:\Penyimpanan Utama\Documents\GitHub\FINAL-PROJECT-STATISTIKA-KOMPUTASI\dataset.xlsx')

# Menghilangkan kolom 'Deskripsi Gejala' jika ada
if 'Deskripsi Gejala' in df_train.columns:
    df_train.drop('Deskripsi Gejala', axis=1, inplace=True)

# Memastikan tipe data numerik untuk kolom nilai gejala
df_train['Nilai Gejala Berat (T3)'] = pd.to_numeric(df_train['Nilai Gejala Berat (T3)'], errors='coerce')
df_train['Nilai Gejala Sedang (T2)'] = pd.to_numeric(df_train['Nilai Gejala Sedang (T2)'], errors='coerce')
df_train['Nilai Gejala Ringan (T1)'] = pd.to_numeric(df_train['Nilai Gejala Ringan (T1)'], errors='coerce')

# Perhitungan nilai gejala penyakit dari data training
filtered_df_ringan = df_train[df_train['Nilai Gejala Ringan (T1)'] > 0.1]
Nilai_Awal_Ringan = filtered_df_ringan['Nilai Gejala Ringan (T1)'].sum()
filtered_df_sedang = df_train[df_train['Nilai Gejala Sedang (T2)'] > 0.1]
Nilai_Awal_Sedang = filtered_df_sedang['Nilai Gejala Sedang (T2)'].sum()
filtered_df_berat = df_train[df_train['Nilai Gejala Berat (T3)'] > 0.1]
Nilai_Awal_Berat = filtered_df_berat['Nilai Gejala Berat (T3)'].sum()

# Perhitungan nilai bobot dari data training
Nilai_Bobot_Ringan = Nilai_Awal_Ringan / 3
Nilai_Bobot_Sedang = Nilai_Awal_Sedang / 3
Nilai_Bobot_Berat = Nilai_Awal_Berat / 3

# Fungsi untuk memprediksi tingkat stress berdasarkan nilai gejala
def predict_stress(total_nilai_ringan, total_nilai_sedang, total_nilai_berat):
    prior_ringan = Nilai_Bobot_Ringan
    likelihood_ringan = total_nilai_ringan
    PxL_ringan = prior_ringan * likelihood_ringan

    prior_sedang = Nilai_Bobot_Sedang
    likelihood_sedang = total_nilai_sedang
    PxL_sedang = prior_sedang * likelihood_sedang

    prior_berat = Nilai_Bobot_Berat
    likelihood_berat = total_nilai_berat
    PxL_berat = prior_berat * likelihood_berat

    posterior_ringan = PxL_ringan / (PxL_ringan + PxL_sedang + PxL_berat)
    posterior_sedang = PxL_sedang / (PxL_ringan + PxL_sedang + PxL_berat)
    posterior_berat = PxL_berat / (PxL_ringan + PxL_sedang + PxL_berat)

    if posterior_ringan > posterior_sedang and posterior_ringan > posterior_berat:
        return 'Ringan'
    elif posterior_sedang > posterior_berat:
        return 'Sedang'
    else:
        return 'Berat'

# Fungsi untuk menginputkan gejala dan menghitung tingkatan stres
def input_gejala_dan_prediksi(df):
    kode_input = input('Masukkan Kode Gejala (Misal : G1,G3,G7,G8,G9)').split(',')
    
    # Inisialisasi total nilai gejala
    total_nilai_ringan = 0
    total_nilai_sedang = 0
    total_nilai_berat = 0
    
    for kode in kode_input:
        kode = kode.strip()
        if kode in df['Kode Gejala'].values:
            total_nilai_ringan += df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
            total_nilai_sedang += df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
            total_nilai_berat += df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
        else:
            print(f'Kode gejala {kode} tidak ditemukan dalam dataset.')
    
    stress = predict_stress(total_nilai_ringan, total_nilai_sedang, total_nilai_berat)
    print(f'\nBerdasarkan gejala yang Anda masukkan, Anda mengalami Stress {stress.capitalize()}.\n')

# Panggil fungsi untuk input gejala dan prediksi
input_gejala_dan_prediksi(df_train)

# Membaca dataset uji dari file Excel
df_test = pd.read_excel('c:\\Users\\LENOVO\\Downloads\\data uji.xlsx')

# Fungsi untuk menjalankan algoritma pada setiap baris dataset uji
def run_algorithm_on_test_data(df_test, df_train):
    results = []
    for index, row in df_test.iterrows():
        kode_input = [row['Gejala 1'], row['Gejala 2'], row['Gejala 3'], row['Gejala 4'], row['Gejala 5']]
        total_nilai_ringan = 0
        total_nilai_sedang = 0
        total_nilai_berat = 0
        
        for kode in kode_input:
            kode = kode.strip()
            if kode in df_train['Kode Gejala'].values:
                total_nilai_ringan += df_train.loc[df_train['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
                total_nilai_sedang += df_train.loc[df_train['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
                total_nilai_berat += df_train.loc[df_train['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
        
        stress = predict_stress(total_nilai_ringan, total_nilai_sedang, total_nilai_berat)
        results.append(stress)
    
    return results

# Menjalankan algoritma pada dataset uji dan menambahkan hasil prediksi ke dataset uji
df_test['Predicted Stress'] = run_algorithm_on_test_data(df_test, df_train)

# Menampilkan hasil prediksi
print(df_test[['Gejala 1', 'Gejala 2', 'Gejala 3', 'Gejala 4', 'Gejala 5', 'Predicted Stress']])