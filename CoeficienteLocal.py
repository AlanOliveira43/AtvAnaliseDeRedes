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

    # Adicione nós à rede
nodes = df.columns.tolist()
net.add_nodes(nodes)

    # Adicione arestas à rede
for i, row in df.iterrows():
        edges = [(nodes[i], nodes[j]) for j, val in enumerate(row) if val == 1]
        net.add_edges(edges)

def calculate_local_clustering_coefficient(node):
        neighbors = net.neighbors(node)
        num_neighbors = len(neighbors)
        if num_neighbors < 2:
            return 0.0
        num_edges = sum([1 if net.has_edge(neighbors[i], neighbors[j]) else 0 for i in range(num_neighbors - 1) for j in range(i + 1, num_neighbors)])
        return 2 * num_edges / (num_neighbors * (num_neighbors - 1))

selected_nodes = st.multiselect("Selecione os nós para calcular o coeficiente de clustering", nodes)

for node in selected_nodes:
        clustering_coefficient = calculate_local_clustering_coefficient(node)
        st.write(f"Coeficiente de Clustering Local para o nó {node}: {clustering_coefficient}")

st.write(net.show("graph.html"), unsafe_allow_html=True)
