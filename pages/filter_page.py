import streamlit as st
import pandas as pd

pokemon_df = pd.read_csv("data\pokemon.csv")
# CODIGO QUE RETIRA OS DUPICADAS DE NÚMERO DA POKEDEX
pokemon_df = pokemon_df.drop_duplicates(subset='pokedex_number')

basic_information = pokemon_df[['pokedex_number', 'name', 'typing']]
advanced_information = pokemon_df[['pokedex_number', 'name', 'abilities', 'hp', 'can_evolve', 'shape']]
fire_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Fire'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
water_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Water'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
ghost_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Ghost'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
grass_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Grass'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
rock_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Rock'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
ice_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Ice'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
poison_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Poison'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
electric_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Electric'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]
normal_pokemon = pokemon_df.loc[pokemon_df['typing'].str.contains('Normal'), ['pokedex_number', 'name', 'typing', 'abilities', 'hp', 'can_evolve', 'shape']]

st.subheader("Filtros do DF")
option = st.selectbox(
    'Selecione um dos filtros para mostrar os dados:',
    ['Informações Básicas', 'Informações Avançadas', 'Fire Pokémon', 'Water Pokémon', 
     'Ghost Pokémon', 'Grass Pokémon', 'Rock Pokémon', 'Ice Pokémon', 'Poison Pokémon', 
     'Electric Pokémon', 'Normal Pokémon'])

# Exibe os dados correspondentes ao filtro selecionado
if option == 'Informações Básicas':
    st.dataframe(basic_information)
elif option == 'Informações Avançadas':
    st.dataframe(advanced_information)
elif option == 'Fire Pokémon':
    st.dataframe(fire_pokemon)
elif option == 'Water Pokémon':
    st.dataframe(water_pokemon)
elif option == 'Ghost Pokémon':
    st.dataframe(ghost_pokemon)
elif option == 'Grass Pokémon':
    st.dataframe(grass_pokemon)
elif option == 'Rock Pokémon':
    st.dataframe(rock_pokemon)
elif option == 'Ice Pokémon':
    st.dataframe(ice_pokemon)
elif option == 'Poison Pokémon':
    st.dataframe(poison_pokemon)
elif option == 'Electric Pokémon':
    st.dataframe(electric_pokemon)
elif option == 'Normal Pokémon':
    st.dataframe(normal_pokemon)
