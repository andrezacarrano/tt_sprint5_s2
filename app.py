import pandas as pd
import streamlit as st
from utils.pre_process import process_dataframe
import plotly.express as px
import os

# Lê arquivo de dados
df_raw = pd.read_csv(r'data/raw/superstore.csv')

# Faz as limpezas iniciais do arquivo de dados
df = process_dataframe(df_raw)

st.title('Superstore Data')

# Toggle para visualizar amostra
toggle_amostra = st.toggle("Visualiza amostra dos dados?", value=True)

if toggle_amostra:
    # Escolhe colunas
    columns = st.multiselect(
        label="Quais colunas você quer visualizar?",
        options=df.columns.tolist(),
        default=['order_id', 'sub_category',
                 'product_name', 'quantity', 'profit']
    )

    # Mostra apenas quando o toggle estiver ativado
    st.dataframe(data=df[columns].sample(10, random_state=42))
else:
    # Não mostra nada quando o toggle estiver desativado
    st.info("Ative a opção acima para visualizar uma amostra dos dados.")

# Gráfico (independente do toggle)
graf_barra = px.bar(
    df,
    x='sub_category',
    y='sales',
    title='Total de Vendas por Modo de Envio',
    color='ship_mode',
    barmode='group'
)

st.plotly_chart(graf_barra)
