import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
l = [1,2,3]
G.add_nodes_from(l)
G=nx.complete_graph(10)
nx.draw(G)
plt.show()
