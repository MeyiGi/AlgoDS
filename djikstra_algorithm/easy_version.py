import matplotlib.pyplot as plt
import networkx as nx 
import numpy as np  
import heapq
from typing import List

# ---------------------------------------------------------------------------------------
src = 0
nodes = "0123456789"
edge_list = [
    (0, 1, 1.3), (1, 2, 3), (0, 2, 2.1), (2, 3, 5), 
    (3, 4, 1.11), (4, 5, 2.2), (2, 6, 2.1), (2, 9, 4.1), 
    (5, 6, 2.3), (8, 1, 1.2), (7, 2, 3), (6, 4, 2.6),
    (5, 0, 1.8), (0, 3, 2), (5, 7, 5.1)
] # src, dst, weight
graph_seed = 1201
node_size = 700
node_colors = "lightblue"
src_color = "red"
font_size = 12
width = 1420
height = 1080
dpi = 100
# ---------------------------------------------------------------------------------------


class Node:
    def __init__(self, data):
        self.data = data

class DijkstraAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def getShortestPaths(self, src):
        queue = [(0, src)]
        visited = {}
        parent = {src: None}

        while queue:
            dist, node = heapq.heappop(queue)

            if node in visited:
                continue
            visited[node] = dist

            for neighbor, cost in self.graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (dist + cost, neighbor))
                    if neighbor not in parent:
                        parent[neighbor] = node

        return parent, visited
    
    def reconstruct_path(self, parent, target):
        path = []
        while target is not None:
            path.append(target)
            target = parent[target]
        return path[::-1]
        
class GraphVisualizer:
    # 
    def __init__(self, matrix, shortest_path_values):
        self.matrix = matrix
        self.shortest_path_values = shortest_path_values

    def draw(self):
        # adding edges from adjacensy 
        G = nx.from_numpy_array(np.array(self.matrix), create_using=nx.DiGraph)

        # Generate a layout for the graph (you can choose other layouts if desired)
        pos = nx.planar_layout(G)

        # configuration for size of window
        plt.figure(figsize=(width / dpi, height / dpi), dpi=dpi)

        # Draw the graph
        node_color = [node_colors for _ in G.nodes()]
        node_color[src] = src_color
        nx.draw(
            G, pos,
            node_size=node_size, node_color=node_color, font_size=font_size
        )

        # Draw edge labels to show weights
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=font_size)

        # Add shortest path values as label on nodes
        if self.shortest_path_values:
            labels = {}

            for i in range(len(self.matrix)):
                dist = self.shortest_path_values.get(i, "")
                labels[i] = f"{i}"
                if dist:
                    labels[i] += f" | {dist}"

            nx.draw_networkx_labels(G, pos, labels=labels, font_size=font_size)

        # Show the plot
        plt.show()


class Graph:
    def __init__(self, n: int, auto_initialize=False, use_terminal=False):
        self.use_terminal = use_terminal
        self.size = n
        self.nodes = []
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

        if auto_initialize:
            for data in range(1, n + 1):
                self.nodes.append(Node(data))


    def addNode(self, data: int):
        if len(self.nodes) == self.size:
            return
        
        self.nodes.append(Node(data))

    def addEdge(self, src: int, dst: int, weight: int):
        self.matrix[src][dst] = weight

    def checkEdge(self, src: int, dst: int):
        return self.matrix[src][dst]
    
    def getDictGraph(self):
        paths = {i: [] for i in range(self.size)}
        for i in range(self.size):
            for j in range(self.size):
                weight = self.matrix[i][j]
                if weight != 0: 
                    paths[i].append((j, self.matrix[i][j]))

        return paths


def main():
    graph = Graph(10, auto_initialize=False)
    # adding nodes to graph
    for ch in nodes:
        graph.addNode(ch)

    # creating edges for nodes
    for edge in edge_list:
        graph.addEdge(*edge)

    # djikstra algorith
    dj = DijkstraAlgorithm(graph.getDictGraph())
    parents, shortest_distances = dj.getShortestPaths(src=src)
    print(graph.getDictGraph())
    print("\nPaths to Each Node:")
    for node in shortest_distances:
        path = dj.reconstruct_path(parents, node)
        print(f"to Node {node} distance is {len(path) - 1}: Path = {' -> '.join(map(str, path))}")
    

    # drawing graph
    visializator = GraphVisualizer(graph.matrix, shortest_distances)
    visializator.draw()


if __name__ == "__main__":
    main()