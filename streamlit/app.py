import streamlit as st

#buat title
st.markdown(
    "<h1 style='text-align: center;'>PENDETEKSI TINGKATAN STRES MAHASISWA AKHIR</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "Website Ini Akan Membantu Mendeteksi Tingkat Stres Yang Kalian Miliki &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:"
)


#buat input user
title = st.text_input("Masukan Nama")
st.write("The current movie title is", title)