# Disjoint Set (Union-Find) utility for Kruskal's Algorithm
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


# Kruskal's Algorithm
def kruskal_mst(n, edges):
    ds = DisjointSet(n)
    mst = []
    total_cost = 0

    edges.sort(key=lambda x: x[2])  # sort by weight

    print("\nEdges included in Minimum Spanning Tree:")
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
            print(f"{u} - {v} \tWeight: {weight}")
    
    print(f"\nTotal Cost of MST: {total_cost}")
    return mst, total_cost


# Main function
def main():
    n = int(input("Enter number of vertices (0-indexed): "))
    e = int(input("Enter number of edges: "))
    edges = []

    print("Enter edges in the format: source destination weight")
    while len(edges) < e:
        try:
            u, v, w = map(int, input().split())
            if u >= n or v >= n or u < 0 or v < 0:
                print("Error: Vertex index out of range. Try again.")
                continue
            edges.append((u, v, w))
        except ValueError:
            print("Invalid input format. Please enter 3 integers.")
            continue

    kruskal_mst(n, edges)


if __name__ == "__main__":
    main()
