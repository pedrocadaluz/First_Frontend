import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

#importar caminho
caminho = Path(__file__).resolve().parent / "data" / "ibov.csv"

st.title('Meu primeiro dashboard')

st.markdown(
    '''
    Olá mundo, tudo bem? Vou lhes apresentar um botão, radio, dataframe e um gráfico
    '''
)

# Criar as abas
abas = st.tabs(["Botão", "Radio", "DataFrame", "Gráfico"])

# Conteúdo da aba Botão
with abas[0]:
    st.header("Botão")
    if st.button('Clique aqui'):
        st.text('Você apertou o botão')

# Conteúdo da aba Radio
with abas[1]:
    st.header("Radio")
    opcao = st.radio(
        "Escolha a opção:",
        ('Flamengo', 'Corinthians', 'Palmeiras')
    )

    if opcao == 'Flamengo':
        st.info('Você é um urubu')
    elif opcao == 'Corinthians':
        st.warning('Você é um campeão')
    else: 
        st.error('Você é um perdedor')

# Conteúdo da aba DataFrame
with abas[2]:
    st.header("DataFrame")
    df = pd.read_csv(caminho + "\\ibov.csv")
    st.dataframe(df)

# Conteúdo da aba Gráfico
with abas[3]:
    st.header("Gráfico")
    
    # Estilo do gráfico
    plt.style.use('_mpl-gallery')

    # Dados para o gráfico
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    # Criar a figura e o eixo
    fig, ax = plt.subplots()

    # Gráfico de barras
    ax.bar(x, y, width=1, edgecolor='white', linewidth=0.7)

    # Configurar os eixos
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    # Mostrar o gráfico no Streamlit
    st.pyplot(fig)
