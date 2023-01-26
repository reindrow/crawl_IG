import streamlit as st
import instaloader

st.write("""# Crawling Data Instagram""") 
profil_name= st.text_input("Masukan nama profil instagram : ")
hasil=st.button("Download")

if hasil:
		st.write("*Jika muncul 'profile xx requires login', berarti akun IG yang anda cari bersifat privasi dan yang akan di download hanya berupa foto profil instagram") 
		instaloader.Instaloader().download_profile(profil_name)
		st.success("Berhasil. Silahkan cek folder di perangkat anda")

