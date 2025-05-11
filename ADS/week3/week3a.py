from collections import deque, defaultdict

def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)

def create_graph():
    graph = defaultdict(list)
    num_nodes = int(input("Enter the number of nodes: "))
    
    for i in range(num_nodes):
        node = int(input(f"Enter node {i+1}: "))
        neighbors = list(map(int, input(f"Enter the neighbors of node {node} (space-separated): ").split()))
        for neighbor in neighbors:
            graph[node].append(neighbor)
            graph[neighbor].append(node)  # For undirected graph

    return graph

# Driver code
graph = create_graph()
start_node = int(input("Enter the starting node for traversal: "))
print("\nBFS Traversal: ")
bfs(graph, start_node)
