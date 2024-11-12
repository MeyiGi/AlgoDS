import json
import matplotlib.pyplot as plt
import networkx as nx
import time
import os

def parse_tree(data, edges=None, pos=None, x=0, y=0, layer=1):
    if edges is None:
        edges = []
    if pos is None:
        pos = {}

    if data is None:
        return edges, pos

    # Add current node's position
    pos[data["val"]] = (x, y)

    # Recurse to the left and right child if they exist
    if data["left"] is not None:
        edges.append((data["val"], data["left"]["val"]))
        parse_tree(data["left"], edges, pos, x - 1 / layer, y - 1, layer + 1)
    if data["right"] is not None:
        edges.append((data["val"], data["right"]["val"]))
        parse_tree(data["right"], edges, pos, x + 1 / layer, y - 1, layer + 1)

    return edges, pos

def visualize_tree():
    plt.ion()  # Interactive mode for live updates
    last_modified = None

    while True:
        if os.path.exists("tree.json"):
            modified_time = os.path.getmtime("tree.json")
            if modified_time != last_modified:
                last_modified = modified_time
                
                # Load and parse tree data
                with open("tree.json", "r") as file:
                    try:
                        tree_data = json.load(file)
                    except json.JSONDecodeError:
                        continue  # Skip if file is not ready to be read
                
                # Get edges and positions
                edges, pos = parse_tree(tree_data)
                
                # Create a directed graph and add edges
                G = nx.DiGraph()
                G.add_edges_from(edges)

                # Clear the previous plot and draw the new one
                plt.clf()
                nx.draw(G, pos, with_labels=True, arrows=False,
                        node_size=1000, node_color="skyblue",
                        font_size=10, font_weight="bold", edge_color="gray")
                plt.title("Binary Tree Visualization")
                plt.draw()

        plt.pause(1)

visualize_tree()
