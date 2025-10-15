import pandas as pd
import streamlit as st
from utils.pre_process import adjust_columns_names

# Lê arquivo de dados
df = pd.read_csv(r'data/superstore.csv')

df = adjust_columns_names(df)

st.title('Superstore Data')

st.dataframe(
    data=df
)

st.bar_chart(data=df, x='Ship Mode', y='Total Net Sales')
