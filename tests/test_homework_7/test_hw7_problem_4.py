import networkx as nx
from typing import Tuple, Hashable, Set

import random 
import network_utilities as nu

def test_hw7_problem_4() -> None:
    """
    Problem 4: Create a graph and a partition of the nodes such that 0.5 <= Q <= 0.6.
    Graph must have >= 12 vertices, >= 2 edges, and partition must have >= 3 sets.
    """

    num_nodes = 30
    partition_size = 10 
    num_random_edges = 90

    partition = [set(range(i,i+partition_size)) for i in range(0,num_nodes,partition_size)]

    def get_edges(valid_vertices_1, valid_vertices_2, num_edges):
        return [(random.choice(list(valid_vertices_1)), random.choice(list(valid_vertices_2))) for i in range(num_edges)]

    i = 0
    edges_list = [
        get_edges(set(list(range(num_nodes))), set(list(range(num_nodes))), int(num_random_edges / 3)),
        get_edges(set(partition[0]), set(partition[0]), num_random_edges),
        get_edges(set(partition[1]), set(partition[1]), num_random_edges),
        get_edges(set(partition[2]), set(partition[2]), num_random_edges),

        ]


    full_edge_set = set().union(*edges_list)

    G = nu.vertex_edge_sets_to_graph({i for i in range(num_nodes)}, full_edge_set)

    # Validate structure
    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() >= 12
    assert G.number_of_edges() >= 2

    # Validate partition
    assert len(partition) >= 3
    assert all(len(group) > 0 for group in partition)
    union = set().union(*partition)
    assert union == set(G.nodes())
    assert sum(len(group) for group in partition) == len(union)

    # Check modularity
    q = nx.community.modularity(G, partition)
    assert 0.5 <= q <= 0.6
