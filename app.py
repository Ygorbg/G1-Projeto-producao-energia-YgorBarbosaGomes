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

# Filtros
st.sidebar.header("Filtros")

anos = sorted(df["ano"].unique())
anos_selecionados = st.sidebar.multiselect(
    "Ano",
    anos,
    default=anos
)

meses = sorted(df["mes"].unique())
meses_selecionados = st.sidebar.multiselect(
    "Mês",
    meses,
    default=meses
)

regioes = sorted(df["regiao"].unique())
regioes_selecionadas = st.sidebar.multiselect(
    "Região",
    regioes,
    default=regioes
)

ufs = sorted(df["uf"].unique())
ufs_selecionadas = st.sidebar.multiselect(
    "UF",
    ufs,
    default=ufs
)

fontes = sorted(df["fonte_energia"].unique())
fontes_selecionadas = st.sidebar.multiselect(
    "Fonte de energia",
    fontes,
    default=fontes
)

demandas = sorted(df["nivel_demanda"].unique())
demandas_selecionadas = st.sidebar.multiselect(
    "Nível de demanda",
    demandas,
    default=demandas
)

df_filtrado = df[
    (df["ano"].isin(anos_selecionados)) &
    (df["mes"].isin(meses_selecionados)) &
    (df["regiao"].isin(regioes_selecionadas)) &
    (df["uf"].isin(ufs_selecionadas)) &
    (df["fonte_energia"].isin(fontes_selecionadas)) &
    (df["nivel_demanda"].isin(demandas_selecionadas))
]

st.subheader("Indicadores principais")

if not df_filtrado.empty:

    # Produção total
    producao_total = df_filtrado["producao_mwh"].sum()

    # Fonte predominante
    producao_fonte = (
        df_filtrado.groupby("fonte_energia")["producao_mwh"]
        .sum()
        .sort_values(ascending=False)
    )
    fonte_predominante = producao_fonte.index[0]

    # Percentual renovável médio
    percentual_renovavel = df_filtrado["percentual_renovavel"].mean()

    # Estado com maior produção
    producao_uf = (
        df_filtrado.groupby("uf")["producao_mwh"]
        .sum()
        .sort_values(ascending=False)
    )
    estado_maior_producao = producao_uf.index[0]

    # Consumo total
    consumo_total = df_filtrado["consumo_mwh"].sum()

    # Emissão total de CO₂
    emissao_total = df_filtrado["emissao_co2"].sum()

    # Primeira linha de indicadores
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Produção total",
        f"{producao_total:,.2f} MWh"
    )

    col2.metric(
        "Fonte predominante",
        fonte_predominante
    )

    col3.metric(
        "Percentual renovável",
        f"{percentual_renovavel:.2f}%"
    )

    # Segunda linha de indicadores
    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Estado com maior produção",
        estado_maior_producao
    )

    col5.metric(
        "Consumo total",
        f"{consumo_total:,.2f} MWh"
    )

    col6.metric(
        "Emissão total de CO₂",
        f"{emissao_total:,.2f}"
    )

else:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")

st.divider()

st.subheader("Análise da Produção de Energia")

if not df_filtrado.empty:

    producao_anual = (
        df_filtrado.groupby("ano")["producao_mwh"]
        .sum()
        .reset_index()
    )

    fig_producao = px.line(
        producao_anual,
        x="ano",
        y="producao_mwh",
        markers=True,
        title="Evolução da Produção de Energia"
    )

    fig_producao.update_layout(
        xaxis_title="Ano",
        yaxis_title="Produção (MWh)"
    )

    st.plotly_chart(
        fig_producao,
        use_container_width=True
    )

    col_grafico1, col_grafico2 = st.columns(2)

    # Produção por fonte
    producao_por_fonte = (
        df_filtrado.groupby("fonte_energia")["producao_mwh"]
        .sum()
        .reset_index()
        .sort_values("producao_mwh", ascending=False)
    )

    fig_fonte = px.bar(
        producao_por_fonte,
        x="fonte_energia",
        y="producao_mwh",
        title="Produção por Fonte Energética"
    )

    fig_fonte.update_layout(
        xaxis_title="Fonte de Energia",
        yaxis_title="Produção (MWh)"
    )

    col_grafico1.plotly_chart(
        fig_fonte,
        use_container_width=True
    )

    # Participação das fontes na matriz energética
    fig_matriz = px.pie(
        producao_por_fonte,
        names="fonte_energia",
        values="producao_mwh",
        title="Participação na Matriz Energética",
        hole=0.3
    )

    fig_matriz.update_traces(
        textposition="inside",
        textinfo="percent+label"
    )

    col_grafico2.plotly_chart(
        fig_matriz,
        use_container_width=True
    )

    col_grafico3, col_grafico4 = st.columns(2)

    # Produção por região
    producao_regiao = (
        df_filtrado.groupby("regiao")["producao_mwh"]
        .sum()
        .reset_index()
        .sort_values("producao_mwh", ascending=False)
    )

    fig_regiao = px.bar(
        producao_regiao,
        x="regiao",
        y="producao_mwh",
        title="Produção de Energia por Região"
    )

    fig_regiao.update_layout(
        xaxis_title="Região",
        yaxis_title="Produção (MWh)"
    )

    col_grafico3.plotly_chart(
        fig_regiao,
        use_container_width=True
    )

    # Ranking de produção por estado
    producao_estado = (
        df_filtrado.groupby("uf")["producao_mwh"]
        .sum()
        .reset_index()
        .sort_values("producao_mwh", ascending=True)
    )

    fig_estado = px.bar(
        producao_estado,
        x="producao_mwh",
        y="uf",
        orientation="h",
        title="Ranking de Produção por Estado",
        height=750
    )

    fig_estado.update_layout(
        xaxis_title="Produção (MWh)",
        yaxis_title="UF",
        yaxis=dict(
            categoryorder="total ascending",
            dtick=1
        )
    )

    col_grafico4.plotly_chart(
        fig_estado,
        use_container_width=True
    )

    col_grafico5, col_grafico6 = st.columns(2)

    # Evolução do percentual de energia renovável
    renovavel_anual = (
        df_filtrado.groupby("ano")["percentual_renovavel"]
        .mean()
        .reset_index()
    )

    fig_renovavel = px.line(
        renovavel_anual,
        x="ano",
        y="percentual_renovavel",
        markers=True,
        title="Evolução do Percentual de Energia Renovável"
    )

    fig_renovavel.update_layout(
        xaxis_title="Ano",
        yaxis_title="Percentual Renovável (%)"
    )

    col_grafico5.plotly_chart(
        fig_renovavel,
        use_container_width=True
    )

    # Relação entre produção e consumo
    fig_consumo = px.scatter(
        df_filtrado,
        x="producao_mwh",
        y="consumo_mwh",
        title="Produção × Consumo",
        opacity=0.6
    )

    fig_consumo.update_layout(
        xaxis_title="Produção (MWh)",
        yaxis_title="Consumo (MWh)"
    )

    col_grafico6.plotly_chart(
        fig_consumo,
        use_container_width=True
    )

        # Impacto ambiental
    fig_emissao = px.scatter(
        df_filtrado,
        x="producao_mwh",
        y="emissao_co2",
        color="fonte_energia",
        title="Emissão de CO₂ × Produção de Energia",
        opacity=0.7
    )

    fig_emissao.update_layout(
        xaxis_title="Produção (MWh)",
        yaxis_title="Emissão de CO₂"
    )

    st.plotly_chart(
        fig_emissao,
        use_container_width=True
    )

        # Sazonalidade da produção
    producao_mensal = (
        df_filtrado.groupby("mes")["producao_mwh"]
        .mean()
        .reset_index()
    )

    fig_sazonalidade = px.line(
        producao_mensal,
        x="mes",
        y="producao_mwh",
        markers=True,
        title="Produção Média de Energia por Mês"
    )

    fig_sazonalidade.update_layout(
        xaxis_title="Mês",
        yaxis_title="Produção Média (MWh)",
        xaxis=dict(dtick=1)
    )

    st.plotly_chart(
        fig_sazonalidade,
        use_container_width=True
    )

        # Participação da energia hidrelétrica
    producao_total_ano = (
        df_filtrado.groupby("ano")["producao_mwh"]
        .sum()
    )

    producao_hidreletrica_ano = (
        df_filtrado[
            df_filtrado["fonte_energia"] == "Hidrelétrica"
        ]
        .groupby("ano")["producao_mwh"]
        .sum()
    )

    participacao_hidreletrica = (
        producao_hidreletrica_ano
        .div(producao_total_ano)
        .mul(100)
        .fillna(0)
        .reset_index(name="participacao_percentual")
    )

    fig_hidreletrica = px.line(
        participacao_hidreletrica,
        x="ano",
        y="participacao_percentual",
        markers=True,
        title="Participação da Energia Hidrelétrica ao Longo dos Anos"
    )

    fig_hidreletrica.update_layout(
        xaxis_title="Ano",
        yaxis_title="Participação Hidrelétrica (%)"
    )

    st.plotly_chart(
        fig_hidreletrica,
        use_container_width=True
    )

    st.divider()
    st.subheader("Interpretação dos Resultados")

    # Região com maior produção
    regiao_destaque = (
        df_filtrado.groupby("regiao")["producao_mwh"]
        .sum()
        .idxmax()
    )

    # Correlação entre produção e consumo
    correlacao = df_filtrado[
        ["producao_mwh", "consumo_mwh"]
    ].corr().iloc[0, 1]

    st.write(
        f"No período e nos filtros selecionados, a fonte com maior "
        f"produção é **{fonte_predominante}**. "
        f"A região com maior produção é **{regiao_destaque}**, enquanto "
        f"o estado com maior produção é **{estado_maior_producao}**."
    )

    st.write(
        f"O percentual médio de energia renovável é de "
        f"**{percentual_renovavel:.2f}%**."
    )

    st.write(
        f"A correlação entre produção e consumo é de "
        f"**{correlacao:.3f}**, indicando o grau de associação linear "
        f"entre essas duas variáveis nos dados selecionados."
    )

    st.write(
        "Os gráficos permitem analisar a evolução da produção, a "
        "participação das diferentes fontes energéticas, as diferenças "
        "regionais, a sazonalidade e os impactos ambientais relacionados "
        "à geração de energia."
    )

    st.divider()
    st.subheader("Conclusão Executiva")

    st.write(
        f"A análise dos dados selecionados mostra que **{fonte_predominante}** "
        f"é a fonte com maior produção de energia. A região de maior destaque "
        f"é **{regiao_destaque}** e o estado com maior produção é "
        f"**{estado_maior_producao}**."
    )

    st.write(
        f"A participação média de fontes renováveis é de "
        f"**{percentual_renovavel:.2f}%**. Os resultados apresentados "
        f"permitem acompanhar a composição da matriz energética, comparar "
        f"regiões e estados e observar as relações entre produção, consumo "
        f"e emissão de CO₂."
    )

    st.write(
        "De forma geral, o dashboard permite explorar diferentes cenários "
        "por meio dos filtros e compreender de maneira interativa a evolução "
        "da produção de energia no Brasil entre 2015 e 2024."
    )

    st.divider()
    st.subheader("Tabela Detalhada")

    st.dataframe(
        df_filtrado,
        use_container_width=True,
        hide_index=True
    )