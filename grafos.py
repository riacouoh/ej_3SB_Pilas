import networkx as nx
import matplotlib.pyplot as plt

class Estado:
    def __init__(self, nombre):
        self.nom= nombre
        self.conexiones = [] 
    
    def agregar_conexion(self, end, costo):
        self.conexiones.append((end, costo))
        
class Grafo:
    def __init__(self):
        self.name = "Siete Estados"
        self.estados = {}  
    
    def add_state(self, nom):
        if nom not in self.estados:
            self.estados[nom] = Estado(nom)
    
    def add_arista(self, start, end, cost):
        if start not in self.estados:
            self.add_state(start)
        if end not in self.estados:
            self.add_state(end)
        self.estados[start].agregar_conexion(self.estados[end], cost)
        self.estados[end].agregar_conexion(self.estados[start], cost)
    
    def mostrar_estados_y_conexiones(self):
        print(f"*** Conexiones entre {self.name} ***")
        for state in self.estados.values():
            conexiones = ", ".join([f"{vecino.nom} (costo: {costo})" for vecino, costo in state.conexiones])
            print(f"{state.nom}: {conexiones}")

    def visit_more(self, actual, visited, costo):
        if len(visited) >= len(self.estados):  
            return costo
        mincost = float('inf')
        for vecino, costo_traslado in actual.conexiones:
            nuevo_costo = self.visit_more(vecino, visited + [vecino], costo + costo_traslado)
            mincost = min(mincost, nuevo_costo)
        return mincost        
    
    def visit_once(self, actual, traveled, costo):
        if len(traveled) == len(self.estados):  
            return costo
        mincost = float('inf')
        for vecino, costo_traslado in actual.conexiones:
            if vecino not in traveled:
                nuevo_costo = self.visit_once(vecino, traveled + [vecino], costo + costo_traslado)
                mincost = min(mincost, nuevo_costo)
        return mincost   

    def draw(self):
        G = nx.Graph()
        for estado in self.estados.values():
            for vecino, costo in estado.conexiones:
                G.add_edge(estado.nom, vecino.nom, weight=costo)
        pos = nx.spring_layout(G) 
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="pink", font_size=10, font_weight="bold")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Grafo de Estados con Costos de Traslado")
        plt.show()
grafo = Grafo()
grafo.add_arista("Yucatán", "Quintana Roo", 11)
grafo.add_arista("Yucatán", "Quintana Roo", 0.9)
grafo.add_arista("Campeche", "Quintana Roo", 0.1)
grafo.add_arista("Campeche", "Tabasco", 0.75)
grafo.add_arista("Quintana Roo", "Chiapas", 0.01)
grafo.add_arista("Chiapas", "Puebla", 0.3)
grafo.add_arista("Chiapas", "Guanajuato", 0.5),
grafo.add_arista("Tabasco", "Puebla", 0.8)
grafo.add_arista("Puebla", "Guanajuato", 0.5)


grafo.mostrar_estados_y_conexiones()

startS= grafo.estados["Puebla"]
costo_sin_repetir = grafo.visit_once(startS, [startS], 0)
costo_con_repeticion = grafo.visit_more(startS, [startS], 0)

print(f"\nCosto total no repeats:{costo_sin_repetir}", )
print(f"Costo total con repeats:{costo_con_repeticion}")

grafo.draw()