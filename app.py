import pandas as pd
import streamlit as st
import plotly.express as px

# Lê arquivo de dados
df = pd.read_csv(r'superstore.csv')

st.title('Superstore Data')

st.dataframe(
    data=df
)

st.bar_chart(data=df, x='Ship Mode', y='Sales')
