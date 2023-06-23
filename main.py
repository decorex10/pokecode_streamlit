import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import streamlit as st
import pandas as pd


names = ["Misty", "Dawn"]
usernames = ["Misty", "Dawn"]

# carregar as senhas
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# cookie json para autenticar sem necessitar inserir dados a cada atualização de pag
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

# tela de login produzida pela biblioteca da streamlit
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Dados incorretos!")

if authentication_status == None:
    st.warning("Insira os dois campos corretamente!")

if authentication_status:

    st.title("Banco de dados ")
    st.header("informações gerais do DF Pokémon:")

    pokemon_df = pd.read_csv("data\pokemon.csv")
    st.dataframe(pokemon_df)

    authenticator.logout("logout", "sidebar")