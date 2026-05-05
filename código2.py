import streamlit as st
import pandas as pd

df = pd.read_csv("deputados_2022.csv")
st. dataframe(df)

#Título do app
st.title("Consulta de Candidatos por Partido")

#Carregar banco de dados CSV
df = pd.read_csv("deputados_2022.csv")

#Entrada do usuário
sigla = st.text_input("Digite a sigla do partido:")

#Filtragem
if sigla:
    resultado = df[df["partido"].str.upper() == sigla.upper()]

    if not resultado.empty:
        st.subheader(f"Candidatos do partido {sigla.upper()}:")
        st.dataframe(resultado)
    else:
        st.warning("Nenhum candidato encontrado para essa sigla.")
