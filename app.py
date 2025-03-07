import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth  
from PIL import Image
from image_classification import currency_classification

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



names = ["Daksh Azad", "Sudiksha Raheja", "Vishal Singh", "Nupur Tyagi"]
usernames = ["dazad", "sraheja", "vsingh", "ntyagi"]




file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,"user_info", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")



if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == True:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.title("Indian Currency Classifier")
    st.header("Classifies Indian Currency")

    uploaded_file = st.file_uploader("Upload here",type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Note', use_column_width=True)
        st.write("")
        st.write("Classifying...")
        st.write("Just a minute")
        label, acc = currency_classification(image)

        switcher = {
                0:"100",
                1:"200",
                2:"2000",
                3:"500",
                4:"50",
                5:"10",
                6:"20"
        }
        s=switcher.get(label, "Not Matching")
        st.write("Done..")
        if s=="Not Matching":
            st.write("Enter valid Image")
        else :
            st.write("This is ", s," rupees note")



