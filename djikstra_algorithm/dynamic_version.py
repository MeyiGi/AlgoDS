import matplotlib.pyplot as plt
import networkx as nx
import numpy as np  
import heapq
from typing import List
import matplotlib.animation as animation
from matplotlib.widgets import Button

# ---------------------------------------------------------------------------------------
src = 0
nodes = "0123456789"
# edge_list = [(0, 1, 1), (1, 2, 1), (0, 2, 1), (2, 3, 1), 
#         (3, 4, 1), (4, 5, 1), (2, 6, 1), (2, 9, 1), 
#         (5, 6, 1), (8, 1, 1), (7, 2, 1), (6, 4, 1),
#         (5, 0, 1), (0, 3, 1), (5, 7, 1)]

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
        self.positions = None
        self.G = None
        self.visited = {}

    def getShortestPaths(self, src):
        queue = [(0, src)]
        parent = {src: None}
        step_data = []  # Store the data for each step to visualize

        while queue:
            dist, node = heapq.heappop(queue)

            if node in self.visited:
                continue
            self.visited[node] = dist

            # Record the graph state for this step
            step_data.append((node, dist, parent.copy(), self.visited.copy(), list(queue)))

            for neighbor, cost in self.graph[node]:
                if neighbor not in self.visited:
                    heapq.heappush(queue, (dist + cost, neighbor))
                    if neighbor not in parent:
                        parent[neighbor] = node

        return step_data  # Return step data to visualize

    def reconstruct_path(self, parent, target):
        path = []
        while target is not None:
            path.append(target)
            target = parent[target]
        return path[::-1]
        

class GraphVisualizer:
    def __init__(self, matrix, step_data):
        self.matrix = matrix
        self.step_data = step_data
        self.G = nx.from_numpy_array(np.array(self.matrix), create_using=nx.DiGraph)
        self.pos = nx.shell_layout(self.G)  # Use spring layout for the graph positioning
        self.fig, self.ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)

    def draw(self, step_idx):
        # Clear the current plot
        self.ax.clear()

        # Get the step's visited nodes, parent information, and queue state
        node, dist, parent, visited, queue = self.step_data[step_idx]

        # Draw the graph with nodes colored according to visitation status
        node_color = ['lightblue' if n not in visited else 'lightgreen' for n in self.G.nodes()]
        node_color[node] = 'red'  # Highlight current node

        nx.draw(self.G, pos=self.pos, ax=self.ax, node_size=node_size, node_color=node_color, font_size=font_size)
        edge_labels = nx.get_edge_attributes(self.G, "weight")
        nx.draw_networkx_edge_labels(self.G, pos=self.pos, ax=self.ax, edge_labels=edge_labels, font_size=font_size)

        # Show shortest path values on the nodes
        labels = {i: f"{i}\n{visited.get(i, '')}" for i in self.G.nodes()}
        nx.draw_networkx_labels(self.G, pos=self.pos, ax=self.ax, labels=labels, font_size=font_size)

        # Display the current step index
        self.ax.set_title(f"Step {step_idx + 1}")

        # Visualize the queue state on the side
        queue_text = "Queue:\n" + "\n".join([f"({n}, {d})" for n, d in queue])
        self.ax.text(1.05, 0.5, queue_text, transform=self.ax.transAxes, fontsize=12, verticalalignment='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=1'))

        # Show the plot at this step
        plt.draw()


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

class InteractiveVisualizer:
    def __init__(self, graph, step_data):
        self.graph = graph
        self.step_data = step_data
        self.current_step = 0
        self.visualizer = GraphVisualizer(graph.matrix, step_data)
        self.fig = self.visualizer.fig
        self.ax = self.visualizer.ax

        # Create a "Next" button
        ax_button = plt.axes([0.85, 0.05, 0.1, 0.075])
        self.button = Button(ax_button, 'Next')
        self.button.on_clicked(self.next_step)

    def next_step(self, event):
        """Go to the next step in the animation."""
        if self.current_step < len(self.step_data) - 1:
            self.current_step += 1
        self.visualizer.draw(self.current_step)

def main():
    graph = Graph(10, auto_initialize=False)
    # adding nodes to graph
    for ch in nodes:
        graph.addNode(ch)

    # creating edges for nodes
    for edge in edge_list:
        graph.addEdge(*edge)

    # Dijkstra algorithm
    dj = DijkstraAlgorithm(graph.getDictGraph())
    step_data = dj.getShortestPaths(src=src)

    # Create interactive visualizer instance
    interactive_visualizer = InteractiveVisualizer(graph, step_data)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
