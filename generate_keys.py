import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Misty", "Dawn"]
usernames = ["Misty", "Dawn"]
passwords = ['watter', 'fire']

# modulo hash para converter senhas com texto simples em hash USANDO BCRYPT
hashed_passwords = stauth.Hasher(passwords).generate()

# armazenar essas senhas em um arquivo 
file_path = Path(__file__).parent / "hashed_pw.pkl"
# abrir o arquivo em modo binario e salvar as senhas nele
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)