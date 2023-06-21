import streamlit as st
import pandas as pd


st.title("Banco de dados ")
st.header("informações gerais do DF Pokémon:")

pokemon_df = pd.read_csv("data\pokemon.csv")
st.dataframe(pokemon_df)
