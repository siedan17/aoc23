import networkx as nx

if __name__ == "__main__":
    with open("day25_input.txt", "r") as f:
        lines = f.readlines()

    edges = []
    for line in lines:
        line = line.strip()
        a = line.split(": ")
        b = a[1].split()
        for e in b:
            edges.append((a[0], e))

    graph = nx.Graph(edges)
    edge_cut = nx.minimum_edge_cut(graph)

    print(edge_cut)

    remaining_graph = graph.copy()
    remaining_graph.remove_edges_from(edge_cut)

    components = list(nx.connected_components(remaining_graph))
    for c in components:
        print(len(c))
