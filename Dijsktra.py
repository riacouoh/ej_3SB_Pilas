def Dijkstra(grafo, origen, destino):
    
    L = {(origen, nodo): float('inf') for nodo in grafo}  
    L[(origen, origen)] = 0  
    S = set()  
    camino_previo = {nodo: None for nodo in grafo}  

    while len(S) < len(grafo):

        u = min(((origen, nodo) for nodo in grafo if (origen, nodo) not in S), key=lambda nodo: L[nodo])

        S.add(u)

        for v, peso in grafo[u[1]].items():
            if (origen, v) not in S:
                if peso == 'inf':
                    peso = float('inf')
                if L[u] + peso < L[(origen, v)]:
                    L[(origen, v)] = L[u] + peso
                    camino_previo[v] = u[1] 
    nodo_actual = destino
    camino = []
    while nodo_actual is not None:
        camino.insert(0, nodo_actual) 
        nodo_actual = camino_previo[nodo_actual]

    return L, camino


grafo = {
    'a': {'b': 4, 'c': 2, 'd': float('inf'), 'e': float('inf'), 'z': float('inf')},
    'b': {'a': 4, 'c': 1, 'd': 5, 'e': float('inf'), 'z': float('inf')},
    'c': {'a': 2, 'b': 1, 'd': 8, 'e': 10, 'z': float('inf')},
    'd': {'a': float('inf'), 'b': 5, 'c': 8, 'e': 2, 'z': 6},
    'e': {'a': float('inf'), 'b': float('inf'), 'c': 10, 'd': 2, 'z': 3},
    'z': {'a': float('inf'), 'b': float('inf'), 'c': float('inf'), 'd': 6, 'e': 3}
}

nodo_origen = 'a'
nodo_destino = 'z'
distancias, camino = Dijkstra(grafo, nodo_origen, nodo_destino)
distancia_total = distancias[(nodo_origen, nodo_destino)]

print("Distancias mínimas:", {f"{nodo_origen}-{nodo}": distancia for (origen, nodo), distancia in distancias.items() if origen == nodo_origen})
print(f"El camino más corto desde el nodo {nodo_origen} hasta el nodo {nodo_destino} es: {', '.join(camino)}, con una longitud de {distancia_total}")
