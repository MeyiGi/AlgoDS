import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self, n: int, auto_initialize=False):
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

    def addEdge(self, src: int, dst: int):
        self.matrix[src][dst] = 1

    def checkEdge(self, src: int, dst: int):
        return self.matrix[src][dst]
    
    def print(self):
        
        # printing nodes to top of matrix
        print("% ", end="")
        for node in self.nodes:
            print(node.data, end=" ")
        print()

        # printing src, dst of matrix
        for i in range(self.size):
            
            print(self.nodes[i].data, end=" ") # it is for left nodes in matrix

            for j in range(self.size):
                print(f"{self.matrix[i][j]}", end=" ")
            print()

    def draw(self):
        g = nx.DiGraph()

        for node in self.nodes:
            g.add_node(node.data)

        for i in range(self.size):
            for j in range(self.size):
                if self.matrix[i][j]:
                    g.add_edge(self.nodes[i].data, self.nodes[j].data)
        
        dpi = 100
        fig = plt.figure(figsize=(12.8, 7.8), dpi=dpi)

        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, node_color="lightblue", node_size=200, font_size=12)
        plt.title("Graph visualization")
        plt.show()


def main():
    obj = Graph(10, auto_initialize=False)
    
    # adding nodes A, B, C, D and E
    for ch in "0123456789":
        obj.addNode(ch)

    # creating edges for nodes
    obj.addEdge(0, 1)
    obj.addEdge(1, 2)
    obj.addEdge(0, 2)
    obj.addEdge(2, 3)
    obj.addEdge(3, 4)
    obj.addEdge(4, 5)
    obj.addEdge(2, 6)
    obj.addEdge(2, 8)
    obj.addEdge(2, 9)
    obj.addEdge(5, 6)
    obj.addEdge(8, 1)
    obj.addEdge(7, 2)
    obj.addEdge(6, 4)

    # printing result
    obj.print()

    obj.draw()


if __name__ == "__main__":
    main()