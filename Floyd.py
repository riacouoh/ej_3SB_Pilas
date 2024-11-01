def floyd_warshall(dist):

    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

inf = float('inf')
graph = [
    [0,   2, inf,   5],
    [inf, 0,   1, inf],
    [inf, inf, 0,   4],
    [3,   inf, inf, 0]
]

distances = floyd_warshall(graph)


city_labels = ['A', 'B', 'C', 'D']
print("Matriz de distancias mínimas:")
for row in distances:
    print(row)

print("\nDistancias mínimas específicas:")
for i, origin in enumerate(city_labels):
    for j, destination in enumerate(city_labels):
        print(f"Distancia mínima de {origin} a {destination}: {distances[i][j]}")
