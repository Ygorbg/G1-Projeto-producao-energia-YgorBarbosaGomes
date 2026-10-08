# ⚡ Produção de Energia no Brasil

## Projeto G1 — Análise e Visualização de Dados com Python

**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Professor:** Alexandre Neves Louzada  
**Aluno:** Ygor Barbosa Gomes

---

## 📌 Sobre o Projeto

Este projeto apresenta uma análise da produção de energia no Brasil entre os anos de 2015 e 2024.

A análise considera diferentes fontes de geração de energia, regiões e estados brasileiros, além de informações relacionadas ao consumo, participação de fontes renováveis, emissão de CO₂ e capacidade instalada.

O projeto também conta com um dashboard interativo desenvolvido em Streamlit e Plotly, permitindo explorar os dados por meio de diferentes filtros.

---

## 🎯 Objetivos

O projeto busca:

- Identificar as principais fontes de energia;
- Comparar a produção entre regiões e estados;
- Analisar a evolução das fontes renováveis;
- Investigar a sazonalidade da produção;
- Avaliar a participação das fontes na matriz energética;
- Analisar a relação entre produção e consumo;
- Avaliar aspectos relacionados à emissão de CO₂;
- Investigar a participação da energia hidrelétrica ao longo dos anos.

---

## 📊 Indicadores Principais

O dashboard apresenta os seguintes KPIs:

1. Produção total de energia;
2. Fonte predominante;
3. Percentual renovável;
4. Estado com maior produção;
5. Consumo total;
6. Emissão total de CO₂.

---

## 🔎 Filtros Interativos

O dashboard permite filtrar os dados por:

- Ano;
- Mês;
- Região;
- Estado (UF);
- Fonte de energia;
- Nível de demanda.

---

## 📈 Visualizações

Foram desenvolvidas visualizações interativas para analisar:

- Evolução da produção de energia;
- Produção por fonte energética;
- Participação das fontes na matriz energética;
- Produção por região;
- Ranking de produção por estado;
- Evolução do percentual de energia renovável;
- Relação entre produção e consumo;
- Emissão de CO₂ × produção;
- Sazonalidade da produção;
- Participação da energia hidrelétrica ao longo dos anos.

---

## 💡 Principais Resultados

Considerando a base completa analisada:

- A **Hidrelétrica** apresentou a maior produção acumulada;
- A região **Nordeste** apresentou a maior produção regional;
- O **Espírito Santo (ES)** apresentou a maior produção entre as UFs;
- A correlação entre produção e consumo foi de aproximadamente **0,977**, indicando forte associação linear positiva;
- O percentual médio de energia renovável foi de **80,83% em 2015** e **80,83% em 2024**;
- A participação hidrelétrica passou de aproximadamente **37,28% em 2015 para 36,90% em 2024**, indicando uma pequena redução.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- SQLAlchemy
- SQLite
- Matplotlib
- Seaborn
- Google Colab
- GitHub

---

## 🗄️ Banco de Dados

Como recurso adicional, os dados também foram armazenados em um banco de dados **SQLite** utilizando **SQLAlchemy**.

Foi realizada uma consulta SQL para agrupar a produção total de energia por região, demonstrando a utilização de persistência e consulta dos dados.

---

## 📁 Estrutura do Projeto

```text
projeto-producao-energia/
├── app.py
├── requirements.txt
├── README.md
├── index.html
├── dados/
│   └── simulacao_producao_energia_brasil.csv
├── notebooks/
│   └── analise_producao_energia.ipynb
├── database/
│   └── producao_energia.sqlite
└── imagens/

## 🌐 Publicação
O projeto será disponibilizado através de:
- GitHub: repositório completo do projeto;
- GitHub Pages: página de apresentação;
- Streamlit Cloud: dashboard interativo.
Os links serão adicionados após a publicação.

## 📝 Conclusão
A análise permitiu observar a composição e a evolução da produção de energia no Brasil entre 2015 e 2024.
Os resultados destacam a participação da energia hidrelétrica, as diferenças de produção entre regiões e estados e a forte relação observada entre produção e consumo.
O dashboard desenvolvido possibilita explorar diferentes cenários de maneira interativa, facilitando a compreensão dos indicadores energéticos e da composição da matriz analisada.

## 👤 Autor
Ygor Barbosa Gomes
Projeto desenvolvido para a disciplina Linguagem de Programação — Análise e Visualização de Dados com Python, ministrada pelo professor Alexandre Neves Louzada.