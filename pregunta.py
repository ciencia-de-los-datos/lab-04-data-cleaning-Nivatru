"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
from datetime import datetime

def fecha(x):
    y = x.split('/')
    if len(y[2]) == 2:
        return pd.to_datetime(x, format='%Y/%m/%d').strftime('%Y-%m-%d')
    return pd.to_datetime(x, dayfirst=True).strftime('%Y-%m-%d')

def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df.drop(df.columns[0], axis = 1, inplace=True)
    df.dropna(axis=0, inplace=True)
    df["sexo"] = df["sexo"].str.lower()
    df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["barrio"] = df["barrio"].str.lower().str.replace("_", " ").str.replace("-", " ")
    df["estrato"] = df["estrato"].astype(int)
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(fecha)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",", "").str.replace("$ ", "").str.replace(".00", "").astype(int)
    df["línea_credito"] = df["línea_credito"].str.lower().str.replace("-", " ").str.replace("_", " ").str.replace(". ", ".")
    df.drop_duplicates(inplace=True)

    return df
