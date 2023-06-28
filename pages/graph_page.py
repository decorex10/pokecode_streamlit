import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

pokemon_df = pd.read_csv("data\pokemon.csv")
# CODIGO QUE RETIRA OS DUPICADAS DE NÚMERO DA POKEDEX
pokemon_df = pokemon_df.drop_duplicates(subset='pokedex_number')

type_information = pokemon_df['typing'].value_counts()
format_information = pokemon_df['shape'].value_counts()
gen_information = pokemon_df['gen_introduced'].value_counts()

st.subheader("Filtros do DF")
st.text("Cada uma das opções irá retornar um gráfico distinto com base em um filtro de dados")
option = st.selectbox(
    'Selecione um dos filtros para mostrar os dados:',
    ['Quantidade de espécies por tipo', 'Quantidade de espécies por formato', 'Quantidade de espécies por geração', 'Gráfico de dispersão'])

# Exibe os dados correspondentes ao filtro selecionado
if option == 'Quantidade de espécies por tipo':
    st.text("Apresenta um gráfico contando a quantidade de pokémon por cada tipo existente")
    st.text("Ele inclui os pokemon que possuem dois tipos, e os subdivide")
    st.markdown("<br>", unsafe_allow_html=True)
    st.line_chart(type_information)
elif option == 'Quantidade de espécies por formato':
    st.text("Apresenta um gráfico que contabiliza a quantidade de pokemon definidos pelo formato")
    st.markdown("<br>", unsafe_allow_html=True)
    st.line_chart(format_information)
elif option == 'Quantidade de espécies por geração':
    st.text("Gráfico que explicita nitidamente a quantidade de pokemon lançadas por geração")
    st.markdown("<br>", unsafe_allow_html=True)
    st.bar_chart(gen_information.sort_index())
elif option == 'Gráfico de dispersão':
    st.text("Gráfico de dispersão que relaciona altura e peso dos pokemon")
    st.text("Utilizando a biblioteca matplotlib")
    st.markdown("<br>", unsafe_allow_html=True)
    fig, ax = plt.subplots()
    ax.scatter(pokemon_df['height'], pokemon_df['weight'])
    ax.set_xlabel('Altura')
    ax.set_ylabel('Peso')
    ax.set_title('Relação entre Altura e Peso dos Pokémon')
    st.pyplot(fig)
