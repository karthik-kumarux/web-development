import sys


# Function to find the vertex with the minimum key value
def min_key(key, mst_set, n):
    min_val = sys.maxsize
    min_index = -1

    for v in range(n):
        if not mst_set[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v
    return min_index


# Prim's Algorithm function
def prim_mst(graph, n):
    key = [sys.maxsize] * n  # Initialize all keys as infinite
    parent = [None] * n  # To store constructed MST
    key[0] = 0  # First vertex is always included
    mst_set = [False] * n  # To keep track of vertices included in MST
    parent[0] = -1  # First node is root

    for _ in range(n - 1):  # Corrected loop range
        u = min_key(key, mst_set, n)
        mst_set[u] = True

        # Update key and parent index of adjacent vertices
        for v in range(n):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    # Print MST result
    print("\nEdge \tWeight")
    total_cost = 0
    for i in range(1, n):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
        total_cost += graph[i][parent[i]]

    print(f"Total Cost of MST: {total_cost}")


# Main function to take input
def main():
    n = int(input("Enter number of vertices: "))
    print("Enter the adjacency matrix (enter 0 if no edge exists):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        graph.append(row)

    prim_mst(graph, n)


if __name__ == "__main__":
    main()
