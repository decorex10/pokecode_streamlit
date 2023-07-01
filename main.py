import streamlit as st
import pandas as pd

pokemon_df = pd.read_csv("data\pokemon.csv")
# CODIGO QUE RETIRA OS DUPICADAS DE NÚMERO DA POKEDEX
pokemon_df = pokemon_df.drop_duplicates(subset='pokedex_number')

def search_by_type(pokemon_type):
    result = pokemon_df.loc[pokemon_df['typing'].str.contains(pokemon_type), ['pokedex_number', 'name', 'typing']]
    st.dataframe(result)


def search_by_shape(pokemon_shape):
    result = pokemon_df.loc[pokemon_df['shape'].str.contains(pokemon_shape), ['pokedex_number', 'name', 'shape']]
    st.dataframe(result)


def search_by_gen(pokemon_gen):
    result = pokemon_df.loc[pokemon_df['gen_introduced'] == pokemon_gen, ['pokedex_number', 'name', 'gen_introduced']]
    st.dataframe(result)


def search_by_color(pokemon_color):
    result = pokemon_df.loc[pokemon_df['primary_color'].str.contains(pokemon_color), ['pokedex_number', 'name', 'primary_color']]
    st.dataframe(result)


st.title("Banco de dados ")
st.header("Escolha o filtro de busca:")

if st.button('Buscar pelo tipo'):
    types = pokemon_df['typing'].unique()
    pokemon_type = st.selectbox(
        'Pesquise pelo tipo do seu pokemon:',
        (types))
    if pokemon_type:
        search_by_type(pokemon_type)

if st.button('Buscar pelo formato'):
    shapes = pokemon_df['shape'].unique()
    pokemon_shape = st.selectbox(
        'Pesquise pelo formato com que ele se parece:',
        (shapes))
    if pokemon_shape:
        search_by_shape(pokemon_shape)

if st.button('Buscar pela geração'):
    gens = pokemon_df['gen_introduced'].unique()
    pokemon_gen = st.selectbox(
        'Pesquise pela geração em que ele foi lançado:',
        (gens))
    if pokemon_gen:
        search_by_gen(pokemon_gen)

if st.button('Buscar pela coloração'):
    colors = pokemon_df['primary_color'].unique()
    pokemon_color = st.selectbox(
        'Pesquise pela sua cor principal:',
        (colors))
    if pokemon_color:
        search_by_color(pokemon_color)



st.dataframe(pokemon_df)
