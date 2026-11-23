import networkx as nx
import matplotlib.pyplot as plt

def visualize_debrujin(graph: dict[str, list[str]]) -> None:
    """
    Visualizes a De Brujin graph using networkx.

    Arguments:
    ----------
        graph: `dict[str, list[str]]`. The adjacency list representative of the De Brujin graph to visualize. 
    """

    G = nx.MultiDiGraph()

    #converting adjacency list into a networkx graph
    for node, neighbors in graph.items():
        G.add_node(node)

        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    #determining the positions of each node using spring layout
    position = nx.spring_layout(G)

    #creating a canvas to draw on
    fig, ax = plt.subplots(figsize = (9, 6))

    #drawing nodes
    nx.draw_networkx_nodes(G, position, 
                           ax = ax, 
                           node_size = 500, 
                           node_color = "lightblue", 
                           edgecolors = "black"
                           )

    #labelling nodes
    nx.draw_networkx_labels(G, position, 
                            ax = ax, 
                            font_size = 11, 
                            font_weight = "bold"
                            )


    #drawing directed edges individually to see parallel edges
    for u, v, key in G.edges(keys = True):

        radius = 0.15 + (key * 0.2)

        nx.draw_networkx_edges(G, position, 
                               ax = ax,
                               edgelist = [(u, v, key)],
                               arrows = True,
                               arrowsize = 20,
                               node_size = 1500,
                               connectionstyle = f"arc3,rad={radius}"
                               )

    ax.set_title("De Brujin Graph")
    plt.tight_layout()
    plt.show()