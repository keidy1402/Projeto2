import streamlit as st
import pandas as pd

# Carregar CSV
df = pd.read_csv("candidatos.csv")

st.title("Consulta de Candidatos por Partido")

# Input do usuário
sigla = st.text_input("Digite a sigla do partido:")

# Resultado filtrado
if sigla:
    resultado = df[
        df["PARTIDO"].str.strip().str.upper() == sigla.strip().upper()
    ]

    if not resultado.empty:
        st.subheader(f"Candidatos do partido {sigla.upper()}")
        st.dataframe(resultado)
    else:
        st.warning("Nenhum candidato encontrado.")

# ------------------------
# GRÁFICO GERAL ABAIXO
# ------------------------
st.subheader("Gráfico Geral de Candidatos por Partido")

grafico = df["PARTIDO"].value_counts()

st.bar_chart(grafico)
