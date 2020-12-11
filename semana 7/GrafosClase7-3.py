import networkx as nx 
import matplotlib.pyplot as plt
G = nx.Graph()
l = [1,2,3]
G.add_nodes_from(l)
G = nx.gnp_random_graph(20,0.5)
nx.draw(G)
plt.show()
