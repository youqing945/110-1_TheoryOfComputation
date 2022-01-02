import pygraphviz as pgv

A = pgv.AGraph(directed=True,strict=True)
A.add_edge(1,2)
A.add_edge(1,3)
A.add_edge(2,4)
A.add_edge(2,5)
A.add_edge(5,6)
A.add_edge(5,7)
A.add_edge(3,8)
A.add_edge(3,9)
A.add_edge(8,10)
A.add_edge(8,11)
A.graph_attr['epsilon']='0.01'
print(A.string())
A.write('test.dot')
A.layout('dot')
A.draw('test.png')