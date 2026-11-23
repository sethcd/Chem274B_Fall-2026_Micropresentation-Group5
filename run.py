from de_brujin_graph import build_debruijn_graph
from find_eulerian_path import find_eulerian_path
from assemble_sequence import assemble_sequence
from visualize_debrujin import visualize_debrujin

import networkx as nx
import matplotlib.pyplot as plt

def main():
    """
    Example use script.
    """
    reads = ["ATG", "TGA", "GAT", "ATT", "TTA", "TAC", "ACA"]            #final seq should be ATGATTACA
    graph = build_debruijn_graph(reads, k = 3)

    #print adjacency list representative of the graph
    for node, neighbors in graph.items():
        print(f"{node} -> {neighbors}")

    #find the eulerian path
    path = find_eulerian_path(graph)
    print(f"The eulerian path is: {path}")

    #Assemble the final sequence
    assembled_seq = assemble_sequence(path)
    print(f"The assembled sequence is {assembled_seq}")

    #visualize graph
    visualize_debrujin(graph)

#driver code
if __name__ == "__main__":
    main()