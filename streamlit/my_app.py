import streamlit as st
import pandas as pd
import numpy as np

# Membaca dataset dari file CSV
df = pd.read_csv('C:/Penyimpanan Utama/Documents/GitHub/FINAL-PROJECT-STATISTIKA-KOMPUTASI/Dataset_Stres - dataset.csv')

# Hapus kolom Deskripsi Gejala
df.drop('Deskripsi Gejala', axis=1, inplace=True)

# Mengonversi kolom nilai menjadi numerik
df['Nilai Gejala Berat (T3)'] = pd.to_numeric(df['Nilai Gejala Berat (T3)'], errors='coerce')
df['Nilai Gejala Sedang (T2)'] = pd.to_numeric(df['Nilai Gejala Sedang (T2)'], errors='coerce')
df['Nilai Gejala Ringan (T1)'] = pd.to_numeric(df['Nilai Gejala Ringan (T1)'], errors='coerce')

# Filter berdasarkan gejala yang memiliki nilai lebih dari 0.1
filtered_df_ringan = df[df['Nilai Gejala Ringan (T1)'] > 0.1]
Nilai_Awal_Ringan = filtered_df_ringan['Nilai Gejala Ringan (T1)'].sum()

filtered_df_sedang = df[df['Nilai Gejala Sedang (T2)'] > 0.1]
Nilai_Awal_Sedang = filtered_df_sedang['Nilai Gejala Sedang (T2)'].sum()

filtered_df_berat = df[df['Nilai Gejala Berat (T3)'] > 0.1]
Nilai_Awal_Berat = filtered_df_berat['Nilai Gejala Berat (T3)'].sum()

# Menghitung Nilai Bobot
Nilai_Bobot_Ringan = Nilai_Awal_Ringan / 3
Nilai_Bobot_Sedang = Nilai_Awal_Sedang / 3
Nilai_Bobot_Berat = Nilai_Awal_Berat / 3

# Menambahkan gaya CSS dan animasi
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f5f7fa;
    }
    .main-title {
        text-align: center;
        color: #3d85c6;
        animation: fadeIn 2s;
    }
    .sub-title {
        text-align: center;
        color: #6aa84f;
        margin-bottom: 20px;
        animation: fadeInUp 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    .card {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
        padding: 20px;
        margin: 10px 0;
        animation: fadeIn 2s;
    }
    .dataframe {
        text-align: center;
        color: #333;
        background-color: #fff;
        border: 1px solid #ccc;
        border-radius: 10px;
        font-size: 14px;
    }
    .dataframe th, .dataframe td {
        text-align: center;
        padding: 8px;
    }
    .dataframe th {
        background-color: #3d85c6;
        color: #fff;
    }
</style>
    """,
    unsafe_allow_html=True,
)

# Judul dan Deskripsi
st.markdown("<h1 class='main-title'>✨ PENDETEKSI TINGKAT STRES MAHASISWA AKHIR ✨</h1>", unsafe_allow_html=True)
st.markdown(
    "<h4 class='sub-title'>😊 Selamat Datang! Kami siap membantu Anda mendeteksi tingkat stres Anda.😊 </h4>",
    unsafe_allow_html=True,
)

data = {
    "Kode Gejala": ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9", "G10",
             "G11", "G12", "G13", "G14", "G15", "G16", "G17", "G18", "G19", "G20",
             "G21", "G22", "G23", "G24", "G25", "G26", "G27", "G28", "G29", "G30"],
    "Nama Gejala": [
        "Sakit Pinggang", "Sesak Nafas", "Gangguan Pencernaan Berat", "Keringat Berlebihan", "Nafsu Makan Menurun",
        "Terlalu Peka", "Merasa Putus Asa/Sudah Tidak Punya Harapan", "Merasa Takut", "Tremor(Gemetar Tidak Terkendali)", "Kurang Bersemangat",
        "Sering Emosi/Emosi Tidak Terkontrol", "Sakit Kepala", "Mudah Menangis","Merasa Cemas", "Suasana Hati Mudah Berubah(Moodyan)",
        "Pendiam (Introvert)", "Maag", "Sering Ketegangan Otot di bagian Tertentu(leher, bahu, dan punggung)", "Prestasi Menurun", "Mudah Lelah/Capek",
        "Sering Lupa", "Tidak Fokus (sulit konsentrasi)", "Sulit Tidur", "Hilang Rasa Percaya Diri", "Jantung Berdebar Semakin Meningkat",
        "Kehilangan Rasa Humor", "Mudah Tersinggung/Sensitif", "Pikiran Kacau", "Sering Menyendiri", "Alergi/Gatal-Gatal Pada Kulit"
    ],
}

df2 = pd.DataFrame(data)

st.markdown("<h3 class='main-title'>📋 Tabel Gejala Penyakit 📋</h3>", unsafe_allow_html=True)
st.table(df2)

with st.form(key="form_input"):
    nama = st.text_input("Masukkan Nama 🧑‍🎓:")
    stres_level = st.text_input("Masukkan Kode Gejala Anda 🧠 (Misal: G1, G2, G3):")
    semester = st.selectbox("Pilih Semester Anda 📚:", ("1", "2", "3", "4", "5", "6", "7", "8"), index=0)
    submit_button = st.form_submit_button(label="Submit 🚀")

if submit_button:
    if not nama:
        st.error("🚫 Nama tidak boleh kosong! 🙅‍♂️")
    elif not stres_level:
        st.error("🚫 Tingkat stres tidak boleh kosong! 🛑")
    elif not semester:
        st.error("🚫 Harap isi semester Anda! 🤔")
    else:
        kode_input = [kode.strip() for kode in stres_level.split(',')]
        total_nilai_ringan = 0
        total_nilai_sedang = 0
        total_nilai_berat = 0

        for kode in kode_input:
            if kode in df['Kode Gejala'].values:
                nilai_gejala_ringan = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Ringan (T1)'].values[0]
                total_nilai_ringan += nilai_gejala_ringan

                nilai_gejala_sedang = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Sedang (T2)'].values[0]
                total_nilai_sedang += nilai_gejala_sedang

                nilai_gejala_berat = df.loc[df['Kode Gejala'] == kode, 'Nilai Gejala Berat (T3)'].values[0]
                total_nilai_berat += nilai_gejala_berat

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
            st.success("\U0001F33C Tingkat Stress Anda : Ringan \U0001F33C")
            st.markdown(
                """
                <p style="font-size: 16px; text-align: center;">
                    Mengalami stres ringan adalah hal yang wajar, namun penting untuk segera menanganinya agar tidak berkembang menjadi masalah yang lebih besar.
                </p>
                """,
                unsafe_allow_html=True,
            )
            
            # Dropdown saran untuk stres ringan
            saran_opsi = st.selectbox(
                "\U0001F4A1 Pilih saran yang ingin Anda coba untuk mengatasi stres ringan:",
                [
                    "Peregangan dan Olahraga Ringan \U0001F3C3\u200D\U0001F3FC",
                    "Pernapasan Dalam \U0001F9D8",
                    "Mendengarkan Musik \U0001F3B5",
                    "Hindari Kafein dan Nikotin \u2615\u200D\U0001F6AB",
                    "Curhat ke Teman atau Keluarga \U0001F91D",
                    "Menulis Jurnal \U0001F4D2",
                    "Melakukan Aktivitas yang Disukai \U0001F3A8"
                ],
            )

            # Tampilkan deskripsi saran berdasarkan pilihan
            if saran_opsi == "Peregangan dan Olahraga Ringan \U0001F3C3\u200D\U0001F3FC":
                st.info("Luangkan waktu 10-15 menit untuk berjalan kaki atau melakukan peregangan. Ini bisa membantu melepaskan hormon endorfin yang mengurangi stres.")
            elif saran_opsi == "Pernapasan Dalam \U0001F9D8":
                st.info("Cobalah teknik pernapasan dalam atau meditasi. Duduk dengan nyaman, tutup mata, dan tarik napas dalam-dalam melalui hidung, tahan sebentar, lalu hembuskan perlahan melalui mulut.")
            elif saran_opsi == "Mendengarkan Musik \U0001F3B5":
                st.info("Putar lagu favorit Anda atau musik yang menenangkan. Musik memiliki kekuatan untuk mengubah suasana hati dan memberikan rasa tenang.")
            elif saran_opsi == "Hindari Kafein dan Nikotin \u2615\u200D\U0001F6AB":
                st.info("Bahan-bahan ini bisa meningkatkan kadar stres. Coba ganti dengan air putih, teh herbal, atau jus buah.")
            elif saran_opsi == "Curhat ke Teman atau Keluarga \U0001F91D":
                st.info("Berbagi perasaan dan cerita dengan orang terdekat bisa sangat membantu. Mereka mungkin memberikan perspektif yang berbeda atau hanya menjadi pendengar yang baik.")
            elif saran_opsi == "Menulis Jurnal \U0001F4D2":
                st.info("Tuliskan apa yang membuat Anda stres dan bagaimana perasaan Anda. Ini bisa membantu Anda memproses emosi dan menemukan solusi yang mungkin belum terpikirkan.")
            elif saran_opsi == "Melakukan Aktivitas yang Disukai \U0001F3A8":
                st.info("Lakukan sesuatu yang Anda nikmati, seperti membaca, menggambar, menonton film, atau berkebun. Aktivitas ini bisa menjadi pelarian sejenak dari tekanan.")

            st.markdown(
                "<p style='text-align: center; font-size: 14px;'>Ingatlah, setiap orang memiliki cara berbeda untuk mengatasi stres. Temukan yang terbaik untuk Anda dan tetap semangat! \U0001F33C</p>",
                unsafe_allow_html=True,
            )

        # Menambahkan logika dropdown untuk saran stres sedang
        elif posterior_sedang > posterior_berat and posterior_sedang > posterior_ringan:
            st.success("\U0001F4A1 Tingkat Stress Anda : Sedang \U0001F4A1")
            st.markdown(
                """
                <p style="font-size: 16px; text-align: center;">
                    Stres sedang memerlukan perhatian lebih. Berikut adalah beberapa saran untuk membantu Anda mengatasinya.
                </p>
                """,
                unsafe_allow_html=True,
            )

            # Dropdown saran untuk stres sedang
            saran_opsi_sedang = st.selectbox(
                "\U0001F4A1 Pilih saran yang ingin Anda coba untuk mengatasi stres sedang:",
                [
                    "Olahraga Teratur \U0001F3CB\u200D\U0001F3FC",
                    "Rencana dan Prioritas \U0001F4CB",
                    "Teknik Relaksasi \U0001F9D8",
                    "Batasi Pemicu Stres \U0001F6AB",
                    "Diet Sehat \U0001F96C",
                    "Cari Dukungan \U0001F91D",
                    "Mengembangkan Hobi \U0001F3A8",
                    "Tidur yang Cukup \U0001F4A4",
                    "Berlatih Mindfulness \U0001F5FF",
                    "Pertimbangkan Terapi \U0001F691",
                ],
            )

            # Tampilkan deskripsi saran berdasarkan pilihan
            if saran_opsi_sedang == "Olahraga Teratur \U0001F3CB\u200D\U0001F3FC":
                st.info("Lakukan aktivitas fisik seperti jogging, yoga, atau bersepeda untuk meningkatkan hormon endorfin yang membantu mengurangi stres.")
            elif saran_opsi_sedang == "Rencana dan Prioritas \U0001F4CB":
                st.info("Buat daftar tugas harian dan atur prioritas Anda. Ini membantu mengurangi perasaan kewalahan.")
            elif saran_opsi_sedang == "Teknik Relaksasi \U0001F9D8":
                st.info("Praktikkan teknik seperti meditasi, pernapasan dalam, atau relaksasi otot progresif untuk menenangkan pikiran dan tubuh.")
            elif saran_opsi_sedang == "Batasi Pemicu Stres \U0001F6AB":
                st.info("Identifikasi hal-hal yang memicu stres dan coba kurangi atau hindari paparan terhadapnya.")
            elif saran_opsi_sedang == "Diet Sehat \U0001F96C":
                st.info("Konsumsi makanan bergizi, termasuk sayur, buah, dan protein, untuk menjaga energi dan suasana hati.")
            elif saran_opsi_sedang == "Cari Dukungan \U0001F91D":
                st.info("Berbicaralah dengan teman, keluarga, atau bergabung dengan komunitas pendukung untuk mendapatkan dukungan emosional.")
            elif saran_opsi_sedang == "Mengembangkan Hobi \U0001F3A8":
                st.info("Luangkan waktu untuk hobi atau aktivitas kreatif yang Anda nikmati, seperti melukis, memasak, atau bermain musik.")
            elif saran_opsi_sedang == "Tidur yang Cukup \U0001F4A4":
                st.info("Pastikan Anda tidur selama 7-9 jam setiap malam untuk membantu tubuh pulih dari stres.")
            elif saran_opsi_sedang == "Berlatih Mindfulness \U0001F5FF":
                st.info("Cobalah untuk fokus pada momen saat ini dengan latihan mindfulness, seperti memperhatikan pernapasan atau lingkungan sekitar Anda.")
            elif saran_opsi_sedang == "Pertimbangkan Terapi \U0001F691":
                st.info("Jika stres Anda berlanjut atau memburuk, pertimbangkan untuk berkonsultasi dengan profesional kesehatan mental.")

            st.markdown(
                "<p style='text-align: center; font-size: 14px;'>Jangan lupa untuk merawat diri sendiri dan mencari bantuan jika diperlukan. Anda tidak sendirian! \U0001F4AA</p>",
                unsafe_allow_html=True,
            )

        # Menambahkan logika dropdown untuk saran stres berat
        elif posterior_berat > posterior_ringan and posterior_berat > posterior_sedang:
            st.success("\U0001F6D1 Tingkat Stress Anda : Berat \U0001F6D1")
            st.warning(
                "\U0001F534 Anda disarankan untuk berkonsultasi lebih lanjut mengenai kondisi Anda. Berikut adalah saran yang dapat membantu Anda:",
                icon="⚠️",
            )

            # Dropdown saran untuk stres berat
            saran_opsi_berat = st.selectbox(
                "\U0001F4A1 Pilih saran yang ingin Anda coba untuk mengatasi stres berat:",
                [
                    "Konsultasi dengan Profesional \U0001F691",
                    "Manajemen Waktu yang Ketat \U0001F4C5",
                    "Dukungan Sosial Intensif \U0001F91D",
                    "Program Relaksasi Mendalam \U0001F9D8",
                    "Rawat Diri Secara Intensif \U0001F9D7‍♂️",
                ],
            )

            # Tampilkan deskripsi saran berdasarkan pilihan
            if saran_opsi_berat == "Konsultasi dengan Profesional \U0001F691":
                st.info("Pertimbangkan untuk berkonsultasi dengan psikolog atau psikiater untuk mendapatkan penanganan yang tepat sesuai kebutuhan Anda. Anda juga bisa mencoba layanan seperti [HALODOC](https://www.halodoc.com) untuk konsultasi online.")
            elif saran_opsi_berat == "Manajemen Waktu yang Ketat \U0001F4C5":
                st.info("Buat jadwal harian yang jelas dan realistis untuk membantu mengelola tekanan dan tugas sehari-hari dengan lebih baik.")
            elif saran_opsi_berat == "Dukungan Sosial Intensif \U0001F91D":
                st.info("Carilah dukungan dari teman dekat, keluarga, atau kelompok pendukung untuk berbagi beban emosional Anda.")
            elif saran_opsi_berat == "Program Relaksasi Mendalam \U0001F9D8":
                st.info("Ikuti program relaksasi seperti yoga terapeutik, mindfulness lanjutan, atau retret meditasi untuk membantu mengatasi stres berat.")
            elif saran_opsi_berat == "Rawat Diri Secara Intensif \U0001F9D7‍♂️":
                st.info("Luangkan waktu untuk perawatan diri secara mendalam, seperti spa, refleksi, atau aktivitas yang menenangkan jiwa.")

            st.markdown(
                """
                <p style='text-align: center; font-size: 14px;'>
                    Jika stres Anda terasa sangat berat dan sulit diatasi, segera cari bantuan profesional. Kesehatan mental Anda sangat berharga! \U0001F64F
                </p>
                """,
                unsafe_allow_html=True,
            )
        elif posterior_berat == posterior_ringan and posterior_berat == posterior_sedang and posterior_sedang == posterior_ringan: 
                st.success("Maka anda tidak dapat didiagnosis stress")
        else :
            st.success("terdapat kesalahan dalam pemasukan kode gejala anda ")