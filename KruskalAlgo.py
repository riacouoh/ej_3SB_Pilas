class UnionFind:
    def __init__(self, elementos):
        self.padre = {elemento: elemento for elemento in elementos}
        self.rango = {elemento: 0 for elemento in elementos}

    def raiz(self, u):
        if self.padre[u] != u:
            self.padre[u] = self.raiz(self.padre[u])
        return self.padre[u]

    def unir(self, u, v):
        raiz_u = self.raiz(u)
        raiz_v = self.raiz(v)

        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1

def kruskal(grafo):
    aristas = []
    for u in grafo:
        for v, peso in grafo[u]:
            if (peso, v, u) not in aristas:
                aristas.append((peso, u, v))
    
    aristas.sort()

    uf = UnionFind(grafo.keys())

    agm = []
    for peso, u, v in aristas:
        if uf.raiz(u) != uf.raiz(v):
            uf.unir(u, v)
            agm.append((u, v, peso))

    return agm

ciudades = {
    'San Francisco': [('Denver', 500), ('Chicago', 900), ('Nueva York', 2000), ('Atlanta', 2200)],
    'Denver': [('San Francisco', 500), ('Chicago', 1800), ('Nueva York', 1600), ('Atlanta', 1400)],
    'Chicago': [('San Francisco', 900), ('Denver', 1800), ('Nueva York', 1000), ('Atlanta', 800)],
    'Nueva York': [('San Francisco', 2000), ('Denver', 1600), ('Chicago', 1000), ('Atlanta', 950)],
    'Atlanta': [('San Francisco', 2200), ('Denver', 1400), ('Chicago', 800), ('Nueva York', 950)]
}

agm_ciudades = kruskal(ciudades)
print("Componentes del Árbol de Expansión Mínima (Ejemplo 1):")
for u, v, peso in agm_ciudades:
    print(f"{u} - {v}: {peso}")
print()
