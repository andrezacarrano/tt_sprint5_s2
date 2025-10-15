import pandas as pd
import streamlit as st
from utils.pre_process import process_dataframe

# Lê arquivo de dados
df_raw = pd.read_csv(r'data/raw/superstore.csv')

# Faz as limpezas iniciais do arquivo de dados
df = process_dataframe(df_raw)

# Processa e salva
df = process_dataframe(df_raw)

st.title('Superstore Data')

st.dataframe(
    data=df
)

st.bar_chart(data=df, x='ship_mode', y='sales')
