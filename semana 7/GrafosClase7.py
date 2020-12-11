Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:23:07) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pip install networkx
SyntaxError: invalid syntax
>>> import network as nx
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import network as nx
ModuleNotFoundError: No module named 'network'
>>> import networkx as nx
import 
>>> matplotlib.pyplot as plt
SyntaxError: invalid syntax
>>> import network as nx
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import network as nx
ModuleNotFoundError: No module named 'network'
>>> import networkx as nx
>>> import matplotlib.pyplot as plt
Matplotlib is building the font cache; this may take a moment.
>>> G = nx.Graph()
>>> G.add_node(1)
>>> G.add_node(2)
>>> G.add_node(3)
>>> pint(G.nodes)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    pint(G.nodes)
NameError: name 'pint' is not defined
>>> print(G.nodes)
[1, 2, 3]
>>> print(G.edges)
[]
>>> G.add_edge(1,2)
>>> G.add_edge(2,3)
>>> G.add_edge(1,3)
>>> print(G.edges)
[(1, 2), (1, 3), (2, 3)]
>>> nx.draw(G)
>>> plt.show()
>>> 