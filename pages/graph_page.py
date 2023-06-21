import streamlit as st
import pandas as pd

pokemon_df = pd.read_csv("data\pokemon.csv")
# CODIGO QUE RETIRA OS DUPICADAS DE NÚMERO DA POKEDEX
pokemon_df = pokemon_df.drop_duplicates(subset='pokedex_number')

type_information = pokemon_df['typing'].value_counts()
format_information = pokemon_df['shape'].value_counts()
gen_information = pokemon_df['gen_introduced'].value_counts()

st.subheader("Filtros do DF")
option = st.selectbox(
    'Selecione um dos filtros para mostrar os dados:',
    ['Quantidade de espécies por tipo', 'Quantidade de espécies por formato', 'Quantidade de espécies por geração'])

# Exibe os dados correspondentes ao filtro selecionado
if option == 'Quantidade de espécies por tipo':
    st.line_chart(type_information)
elif option == 'Quantidade de espécies por formato':
    st.line_chart(format_information)
elif option == 'Quantidade de espécies por geração':
    st.bar_chart(gen_information.sort_index())
