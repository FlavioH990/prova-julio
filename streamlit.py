import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("tabela_consolidada.xlsx")
status_contagem = df[df["Status do Processo"].isin(["Aprovado", "Reprovado", "Evasão", "Matriculado"])]["Status do Processo"].value_counts()
top_3_status = df["Status do Processo"].value_counts().nlargest(3)
top_5_etapas_desqualificacao = df["Etapa de Desqualificação_x"].value_counts().nlargest(5)
media_idade_por_status = round(df.groupby("Status do Processo")["Idade"].mean().loc[["Matriculado", "Reprovado"]])
top_5_condicoes_moradia = df["Condições  moradia"].value_counts().nlargest(5)
frequencia_escolaridade = df["Escolaridade_y"].value_counts()
tabela_trabalhando = df["Trabalhando?"].value_counts()
top_5_estados = df["Estado_y"].value_counts().nlargest(5)

st.title("Análise EdN")

st.write("### Status do Processo")
st.bar_chart(status_contagem)

st.write("### Status mais recorrentes")
st.bar_chart(top_3_status)

st.write("### Etapa de Desqualificação")
st.bar_chart(top_5_etapas_desqualificacao)

st.write("### Idade média por Status")
st.bar_chart(media_idade_por_status)

st.write("### Condições de moradia")
st.bar_chart(top_5_condicoes_moradia)

st.write("### Alunos trabalhando")
fig, ax = plt.subplots()
ax.pie(tabela_trabalhando, labels=tabela_trabalhando.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)

st.write("### Estados com mais alunos")
fig, ax = plt.subplots()
ax.pie(top_5_estados, labels=top_5_estados.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)