import streamlit as st
import pandas as pd
import numpy as np

#buat title
st.markdown(
    "<h1 style='text-align: center;'>PENDETEKSI TINGKATAN STRES MAHASISWA AKHIR</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "Website Ini Akan Membantu Mendeteksi Tingkat Stres Yang Kalian Miliki &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)



#Tempat buat naruh tabel penyakit
data = {
    "Kode": ["G1", "G2", "G3", "G4", "G5","G6", "G7", "G8", "G9", "G10",
             "G11", "G12", "G13", "G14", "G15","G16", "G17", "G18", "G19", "G20",
             "G21", "G22", "G23", "G24", "G25","G26", "G27", "G28", "G29", "G30"
            ],
    "Gejala": ["Sakit Pinggang", "Sesak Nafas", "Gangguan Pencernaan Berat", "Keringat Berlebihan", "Nafsu Makan Menurun",
               "Terlalu Peka", "Merasa Putus Asa/Sudah Tidak Punya Harapan", "Merasa Takut", "Tremor(Gemetar Tidak Terkendali)", "Kurang Bersemangat",
               "Sering Emosi/Emosi Tidak Terkontrol", "Sakit Kepala", "Mudah Menangis","Merasa Cemas", "Suasana Hati Mudah Berubah(Moodyan)",
               "Pendiam (Introvert)", "Maag", "Sering Ketegangan Otot di bagian Tertentu(leher, bahu, dan punggung)", "Prestasi Menurun", "Mudah Lelah/Capek",
               "Sering Lupa", "Tidak Fokus (sulit konsentrasi)", "Sulit Tidur", "Hilang Rasa Percaya Diri", "Jantung Berdebar Semakin Meningkat",
               "Kehilangan Rasa Humor", "Mudah Tersinggung/Sensitif", "Pikiran Kacau", "Sering Menyendiri", "Alergi/Gatal-Gatal Pada Kulit"  
              ],
    
}

# Membuat DataFrame
df = pd.DataFrame(data)

st.markdown(
    "<h3 style='text-align: center;'>Tabel Gejala Penyakit</h3>",
    unsafe_allow_html=True
)


st.markdown(
    "<div style='display: flex; justify-content: center;'><div style='text-align: center;'>"
    + df.to_html(index=False)
    + "</div></div>",
    unsafe_allow_html=True,
) 


#buat input user
with st.form(key="form_input"):

    nama = st.text_input("Masukan Nama:")
    stres_level = st.text_input("Masukan Salah Satu Kode Gejala Stres Anda (Sesuai Dengan Tabel Di Atas, Misal: G1,G2,G3):")
    semester = st.selectbox(
        "Masukan Semester Anda:",
        ("1", "2", "3","4","5","6","7","8"),
        index=0,
        placeholder="Masukan Semester",
    )

    submit_button = st.form_submit_button(label="Submit")
    #validasi input
if submit_button:
    if not nama:
        st.error("Nama tidak boleh kosong!")
    elif not stres_level:
        st.error("Tingkat stres tidak boleh kosong!")
    elif not semester:
        st.error("Mohon isi semester Anda!")
    else:
        # Untuk sementara
        st.success("Data berhasil disimpan!")
    

