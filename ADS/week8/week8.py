def floyd_warshall(graph, n):
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    next_node = [[-1 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] != float('inf') and i != j:
                next_node[i][j] = j

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

    print("\nAll pairs shortest paths matrix:")
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
        print()

    def get_path(u, v):
        if next_node[u][v] == -1:
            return []
        path = [u + 1]
        while u != v:
            u = next_node[u][v]
            path.append(u + 1)
        return path

    print("\nShortest paths:")
    for i in range(n):
        for j in range(n):
            if i != j:
                path = get_path(i, j)
                if path:
                    print(f"Path from {i + 1} to {j + 1}: {' -> '.join(map(str, path))}")
                else:
                    print(f"No path from {i + 1} to {j + 1}")


def main():
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (use INF for no edge):")
    graph = []
    for i in range(n):
        while True:
            row = input(f"Row {i + 1}: ").split()
            if len(row) != n:
                print(f"Error: Row {i + 1} must have exactly {n} values. Try again.")
                continue
            row_data = []
            try:
                for val in row:
                    if val.upper() == 'INF':
                        row_data.append(float('inf'))
                    else:
                        row_data.append(int(val))
                graph.append(row_data)
                break
            except ValueError:
                print("Invalid input. Please enter integers or 'INF'. Try again.")
    floyd_warshall(graph, n)


if __name__ == "__main__":
    main()
