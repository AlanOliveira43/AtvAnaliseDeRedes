import streamlit as st
import pandas as pd
from pyvis.network import Network

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "Global.csv"

df = load_data(file_path)

net = Network(directed=False, notebook=True)

# Adicionar nós à rede
nodes = df.columns.tolist()
net.add_nodes(nodes)

# Adicionar arestas à rede
for i, row in df.iterrows():
        edges = [(nodes[i], nodes[j]) for j, val in enumerate(row) if val == 1]
        net.add_edges(edges)

diameter = net.diameter()
periphery = net.get_periphery()

st.write("Diâmetro da rede:", diameter)
st.write("Periferia da rede:", periphery)
st.write(net.show("graph.html"), unsafe_allow_html=True)
