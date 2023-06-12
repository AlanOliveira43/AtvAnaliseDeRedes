import streamlit as st
import pandas as pd
from pyvis.network import Network

# Carregar dados do arquivo CSV
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path, header=None)
    return df

# Carregar arquivo CSV
file_path = "global.csv"

df = load_data(file_path)

# Criar uma instância do objeto Network do Pyvis
net = Network(directed=True, notebook=True, template=None)

# Adicionar nós ao gráfico
num_nodes = len(df.columns)
for node in range(num_nodes):
    net.add_node(node)

# Adicionar arestas ao gráfico
for source in range(num_nodes):
    for target in range(num_nodes):
        if df.iloc[source, target] == 1:
            net.add_edge(source, target)

# Configurar visualização da matriz de adjacência
net.show_buttons(filter_=['physics'])

# Apresentar a matriz de adjacência no Streamlit
st.write(net.show("graph.html"), unsafe_allow_html=True)
