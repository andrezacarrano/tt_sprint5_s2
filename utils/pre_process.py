import pandas as pd
import os


def process_dataframe(dataframe):
    df = dataframe.copy()

    # Ajustar nomes das colunas dentro da função
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(r'\(%\)', '', regex=True)
        .str.strip()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )
    # remover dados nulos
    df = df.dropna()

    # Caminho para salvar o arquivo CSV
    output_path = 'data/processed/superstore_clean.csv'

    # Salva o DataFrame no caminho desejado
    df.to_csv(output_path, index=False)

    return df
