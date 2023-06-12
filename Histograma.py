import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "Global.csv"

df = load_data(file_path)



degree_counts = df.sum(axis=0)
degree_freq = degree_counts.value_counts(normalize=True).sort_index()
cumulative_freq = np.cumsum(degree_freq)

fig, ax = plt.subplots()
ax.bar(degree_freq.index, degree_freq, width=0.8, alpha=0.7)
ax.set_xlabel('Grau')
ax.set_ylabel('Frequência')
ax.set_title('Histograma de Distribuição Empírica de Grau')
st.pyplot(fig)

fig, ax = plt.subplots()
ax.plot(degree_freq.index, cumulative_freq, marker='o')
ax.set_xlabel('Grau')
ax.set_ylabel('Frequência Cumulativa')
ax.set_title('Distribuição Cumulativa de Grau')
st.pyplot(fig)
st.write(net.show("graph.html"), unsafe_allow_html=True)
