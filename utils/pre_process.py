import pandas as pd


def adjust_columns_names(dataframe):
    df = dataframe.copy()

    # Ajustar nomes das colunas dentro da função
    df.columns = (
        df.columns
        .str.lower()
        .str.replace(r'\(%\)', '', regex=True)
        .str.strip()
        .str.replace(' ', '_')
    )
    # remover dados nulos
    df = df.dropna()

    return df
