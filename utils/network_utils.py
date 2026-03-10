import networkx as nx

def generate_network(nodes):
    return nx.erdos_renyi_graph(nodes, 0.2)
