# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to create the graph
def create_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        node = input("Enter the node: ").strip()
        neighbors = input(f"Enter the neighbors of {node} (separated by space): ").strip().split()
        graph[node] = neighbors

    return graph

# Main function
def main():
    graph = create_graph()
    start_node = input("Enter the starting node for DFS: ").strip()

    if start_node not in graph:
        print("Start node not found in the graph.")
        return

    print("DFS Traversal:", end=" ")
    dfs(graph, start_node)
    print()  # for newline after DFS output

if __name__ == "__main__":
    main()
