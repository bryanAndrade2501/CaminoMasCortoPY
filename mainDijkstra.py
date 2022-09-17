from dijGrafo import Grafo

g=Grafo(10)

g.agregarArista(0,1,4)
g.agregarArista(0,6,7)
g.agregarArista(1,6,11)
g.agregarArista(1,7,20)
g.agregarArista(1,2,9)
g.agregarArista(2,3,6)
g.agregarArista(2,4,2)
g.agregarArista(3,4,10)
g.agregarArista(3,5,5)
g.agregarArista(4,5,15)
g.agregarArista(4,7,1)
g.agregarArista(4,8,5)
g.agregarArista(5,8,12)
g.agregarArista(6,7,1)
g.agregarArista(7,8,3)
g.agregarArista(8,9,20)

nodo_inicial=5
Dijkstra = g.dijkstra(nodo_inicial)

for nodo in range(len(Dijkstra)):
    print("La distancia del nodo "+str(nodo_inicial)+" al nodo ",nodo, " es ", Dijkstra[nodo])