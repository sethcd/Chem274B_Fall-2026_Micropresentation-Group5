
def assemble_sequence(path: list[str]) -> str:
    """
    Reconstructs a DNA sequence from a Eulerian path through a De Bruijn graph.

    Arguments:
    ----------
        path: `list[str]`. Eulerian path through a De Bruijn graph, represented by a list of strings.

    Returns:
    --------
        sequence: `str`. The sequence assembled from the eulerian path.
    """

    #error handling
    if not path:
        return ""

    #start at first element in path
    sequence = path[0]

    #join nodes based on last element (overlap)
    for node in path[1:]:
        sequence += node[-1]

    return sequence