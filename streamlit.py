import streamlit as st
import pandas as pd
import os
print(os.getcwd())

df = pd.read_csv("MS_Financial Sample.csv", sep=";")

st.title("Gráfico simples de Vendas por Categoria")



vendas = df.groupby("Product Category")["Revenue"].sum()


st.bar_chart(vendas)
