import pandas as pd
import streamlit as st
from utils.pre_process import process_dataframe
import plotly.express as px

# Lê arquivo de dados
df_raw = pd.read_csv(r'data/raw/superstore.csv')

# Faz as limpezas iniciais do arquivo de dados
df = process_dataframe(df_raw)

# Processa e salva
df = process_dataframe(df_raw)

st.title('Superstore Data')

toggle_amostra = st.toggle("Visualiza amostra dos dados?", value=True)
if toggle_amostra:
    columns = (st.multiselect(
        label="Quais colunas você quer visualizar?",
        options=df.columns.tolist(),
        default=['order_id', 'sub_category',
                 'product_name', 'quantity', 'profit']
    )
    )
    st.dataframe(data=df[columns].sample(10, random_state=42))

st.dataframe(
    data=df[columns]
)

graf_barra = px.bar(df, x='sub_category', y='sales',
                    title='Total de Vendas por Modo de Envio', color='ship_mode', barmode='group')

st.plotly_chart(graf_barra)
