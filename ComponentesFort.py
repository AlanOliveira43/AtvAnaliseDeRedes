import streamlit as st
import pandas as pd
from pyvis.network import Network
import networkx as nx

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

file_path = "Global.csv"

df = load_data(file_path)

net = Network(directed=True, notebook=True)

    # Adicione nós à rede
nodes = df.columns.tolist()
net.add_nodes(nodes)

    # Adicione arestas à rede
for i, row in df.iterrows():
        edges = [(nodes[i], nodes[j]) for j, val in enumerate(row) if val == 1]
        net.add_edges(edges)

graph = nx.DiGraph()
graph.add_edges_from(net.edges())

strongly_connected_components = list(nx.strongly_connected_components(graph))

for idx, component in enumerate(strongly_connected_components):
        st.write(f"Componente Conectado Fortemente #{idx+1}:")
        st.write(component)

st.write(net.show("graph.html"), unsafe_allow_html=True)
