def bellman_ford(vertices, edges, source):
    dist = [float('inf')] * vertices
    dist[source] = 0
    predecessor = [-1] * vertices
    print(f"Initial distances: {dist}")

    for i in range(vertices - 1):
        print(f"\nIteration {i+1}:")
        updated = False  # Flag to check if any distance was updated in this iteration
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
                updated = True
        print(f"Distances: {dist}")
        if not updated:
            print("No more updates in this iteration.")
            break  # Optimization: If no updates, no negative cycle will be found later

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("\nGraph contains a negative-weight cycle")
            return

    print("\nFinal shortest distances from source:")
    for i in range(vertices):
        print(f"Vertex {i}: {dist[i]}")

V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))
edges = []

print("Enter each edge in format: source destination weight (0-based index).")

for _ in range(E):
    try:
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
        if not (0 <= u < V and 0 <= v < V):
            print("Invalid vertex index. Please ensure vertex indices are within the range [0, V-1].")
            exit()
    except ValueError:
        print("Invalid input format. Please enter source, destination, and weight separated by spaces.")
        exit()

source = int(input(f"Enter source Vertex (0 to {V-1}): "))
if not (0 <= source < V):
    print("Invalid source vertex index.")
else:
    bellman_ford(V, edges, source)
