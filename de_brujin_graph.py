def build_debruijn_graph(reads: list[str], k: int) -> dict[str, list[str]]:
    """
    Constructs a directed de Bruijn multigraph from DNA reads using only python built-ins.

    Keys:   (k-1)-mer nodes\n
    Values: lists of outgoing neighboring nodes

    Arguments
    ---------
    reads: 
        List of strings representing the sequencing reads of interest (eg. [ATGCGAGT, ATCTCGTA, ...])
    k:
        integer value denoting the size of the k-mer used to construct the graph
    
    Returns
    -------
    graph:
        The resultant graph constructed as a python dictionary representative of an adjacency list. 
        Keys are (k-1)-mer nodes and values are lists of outgoing neighboring nodes.
    """
    graph = {}

    for read in reads:
        #extract each overlapping k-mer
        for i in range(len(read) - k + 1):
            kmer = read[i:i + k]

            #remove the last and first characters, respectively
            prefix = kmer[:-1]
            suffix = kmer[1:]

            #ensure both nodes exist in the graph
            if prefix not in graph:
                graph[prefix] = []

            if suffix not in graph:
                graph[suffix] = []

            #create the directed edge
            graph[prefix].append(suffix)

    return graph