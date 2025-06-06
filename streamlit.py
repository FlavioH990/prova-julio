import streamlit as st
import pandas as pd


df = pd.read_csv("MS_Financial Sample.csv")

st.title("Gráfico simples de Vendas por Categoria")


vendas = df.groupby("Product Category")["Revenue"].sum()


st.bar_chart(vendas)
