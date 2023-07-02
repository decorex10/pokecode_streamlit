import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="PokeCode",
    page_icon="assets\icons\logo1.png",
    initial_sidebar_state="collapsed"
)

# estilizando com o arquivo css
with open('assets\css\style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

pokemon_df = pd.read_csv("data\pokemon.csv")
# CODIGO QUE RETIRA OS DUPICADAS DE NÚMERO DA POKEDEX
pokemon_df = pokemon_df.drop_duplicates(subset='pokedex_number')
# adicionando os links das imagens em uma nova coluna no banco
pokemon_df['image'] = ''
pokemon_df['image'] = pokemon_df['pokedex_number'].apply(lambda x: f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{x}.png')


def generate_data_editor(result):
    return st.data_editor(
    result,
    column_config={
        "image": st.column_config.ImageColumn(
            "Image"
        )
    },
    hide_index=True,
    )


def search_by_type(pokemon_type):
    result = pokemon_df.loc[pokemon_df['typing'].str.contains(pokemon_type), ['pokedex_number', 'name', 'typing', 'image']]
    return generate_data_editor(result)


def search_by_shape(pokemon_shape):
    result = pokemon_df.loc[pokemon_df['shape'].str.contains(pokemon_shape), ['pokedex_number', 'name', 'shape', 'image']]
    return generate_data_editor(result)


def search_by_gen(pokemon_gen):
    result = pokemon_df.loc[pokemon_df['gen_introduced'] == pokemon_gen, ['pokedex_number', 'name', 'gen_introduced', 'image']]
    return generate_data_editor(result)


def search_by_color(pokemon_color):
    result = pokemon_df.loc[pokemon_df['primary_color'].str.contains(pokemon_color), ['pokedex_number', 'name', 'primary_color', 'image']]
    return generate_data_editor(result)


def search_is_baby():
    result = pokemon_df.loc[pokemon_df['baby_pokemon'] == True, ['pokedex_number', 'name', 'baby_pokemon', 'image']]
    return generate_data_editor(result)


def search_is_legendary():
    result = pokemon_df.loc[pokemon_df['legendary'] == True, ['pokedex_number', 'name', 'legendary', 'image']]
    return generate_data_editor(result)


def search_is_mythical():
    result = pokemon_df.loc[pokemon_df['mythical'] == True, ['pokedex_number', 'name', 'mythical', 'image']]
    return generate_data_editor(result)


# MAIN PAGE START --
st.image("assets\icons\logo2.png")
st.markdown('<h1 class="site-title">Banco de dados</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="site-subt">Escolha o filtro de busca:</h2>', unsafe_allow_html=True)

with st.expander("Buscar pelo tipo"):
    types = pokemon_df['typing'].unique()
    pokemon_type = st.selectbox(
        'Pesquise pelo tipo do seu pokemon:',
        (types))
    if pokemon_type:
        search_by_type(pokemon_type)

with st.expander("Buscar pelo formato"):
    shapes = pokemon_df['shape'].unique()
    pokemon_shape = st.selectbox(
        'Pesquise pelo formato com que ele se parece:',
        (shapes))
    if pokemon_shape:
        search_by_shape(pokemon_shape)

with st.expander("Buscar pela geração"):
    gens = pokemon_df['gen_introduced'].unique()
    pokemon_gen = st.selectbox(
        'Pesquise pela geração em que ele foi lançado:',
        (gens))
    if pokemon_gen:
        search_by_gen(pokemon_gen)

with st.expander("Buscar pela cor"):
    colors = pokemon_df['primary_color'].unique()
    pokemon_color = st.selectbox(
        'Pesquise pela sua cor principal:',
        (colors))
    if pokemon_color:
        search_by_color(pokemon_color)

with st.expander("Buscar os pokémon por raridade"):
    
    rarity = st.radio(
        "",
        ["baby_pokemon", "legendary", "mythical"], 
        horizontal=True
    )
    if rarity == 'baby_pokemon':
        search_is_baby()
    elif rarity == 'legendary':
        search_is_legendary()
    else:
        search_is_mythical()
