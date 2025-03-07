import pickle
from pathlib import Path

import streamlit_authenticator as stauth

names = ["Daksh Azad", "Sudiksha Raheja", "Vishal Singh", "Nupur Tyagi"]
usernames = ["dazad", "sraheja", "vsingh", "ntyagi"]
passwords = ["123", "456", "789", "246"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)