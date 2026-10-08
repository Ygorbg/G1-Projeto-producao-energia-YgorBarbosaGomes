import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Produção de Energia no Brasil",
    layout="wide"
)

st.title("Produção de Energia no Brasil")

st.write(
    "Dashboard de análise e visualização dos dados de produção "
    "de energia no Brasil entre 2015 e 2024."
)

st.markdown("""
**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Professor:** Alexandre Neves Louzada  
**Aluno:** Ygor Barbosa Gomes
""")

st.divider()

# Leitura da base de dados
df = pd.read_csv(
    "dados/simulacao_producao_energia_brasil.csv"
)

df["data"] = pd.to_datetime(df["data"])

st.subheader("Base de dados")

st.write(f"Registros encontrados: {len(df)}")

st.dataframe(
    df.head(),
    use_container_width=True
)