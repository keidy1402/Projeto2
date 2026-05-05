import streamlit as st
import pandas as pd

# Carregar CSV
df = pd.read_csv("deputados_2022.csv")

st.title("🎢 Consulta de Candidatos por Partido")
st.set_page_config(
    page_title="Consulta de Candidatos por Partido",
    page_icon="🎢",
    layout="wide"
)

# Input do usuário
sigla = st.text_input("Digite a sigla do partido:")

# Resultado filtrado
if sigla:
    resultado = df[
        df["partido"].str.strip().str.upper() == sigla.strip().upper()
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

grafico = df["partido"].value_counts()

st.bar_chart(grafico)
