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

net = Network(directed=False, notebook=True)

# Adicione nós à rede
nodes = df.columns.tolist()
net.add_nodes(nodes)

# Adicione arestas à rede
for i, row in df.iterrows():
        edges = [(nodes[i], nodes[j]) for j, val in enumerate(row) if val == 1]
        net.add_edges(edges)

graph = nx.Graph()
graph.add_edges_from(net.edges())

degree_centralities = nx.degree_centrality(graph)

for node, centrality in degree_centralities.items():
        st.write(f"Centralidade de Grau para o nó {node}: {centrality}")

st.write(net.show("graph.html"), unsafe_allow_html=True)
