from algoritmoBellmanFord import Grafo
g=Grafo(5)

g.agregarArista(0,1,2)
g.agregarArista(0,2,4)
g.agregarArista(1,3,2)
g.agregarArista(2,4,3)
g.agregarArista(2,3,4)
g.agregarArista(4,3,-5)

g.bellman_ford(2)