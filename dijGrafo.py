from queue import PriorityQueue

class Grafo:
    def __init__(self, num_nodos):
        self.numNodos=num_nodos #Número de nodos
        self.aristas = [[-1 for i in range(num_nodos)] for j in range(num_nodos)] #Aristas y pesos
        self.visitado=[] #Lista de vértices visitados
    
    def agregarArista(self, origen, destino, peso):
        self.aristas[origen][destino] = peso
        self.aristas[destino][origen] = peso
    
    def dijkstra(self, nodo_inicial):
        D={nodo:float('inf') for nodo in range(self.numNodos)}
        D[nodo_inicial]=0
        
        cp = PriorityQueue()
        cp.put((0,nodo_inicial))       
        
        while not cp.empty():
            
            (dist, nodo_actual) = cp.get()
            print(cp.queue)
            #print(nodo_actual)
            self.visitado.append(nodo_actual)
            
            for vecino in range (self.numNodos):
                if self.aristas[nodo_actual][vecino] != -1:
                    distancia = self.aristas[nodo_actual][vecino]
                    if vecino not in self.visitado:
                        costo_anterior = D[vecino]
                        costo_nuevo = D[nodo_actual]+distancia
                        if costo_nuevo<costo_anterior:
                            cp.put((costo_nuevo, vecino))
                            D[vecino] = costo_nuevo
                            
        return D

