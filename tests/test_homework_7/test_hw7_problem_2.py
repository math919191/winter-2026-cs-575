import networkx as nx
from typing import Tuple, Hashable, Set

import network_utilities as nu
import random

def test_hw7_problem_2() -> None:
    """
    Problem 2: Create a graph and a partition of the nodes such that Q >= 0.95.
    Graph must have >= 5 vertices, >= 2 edges, and partition must have >= 2 sets.
    """

    num_nodes = 100
    partition_size = 2
    num_random_edges_per_partition = 5

    partition = [set(range(i,i+partition_size)) for i in range(0,num_nodes,partition_size)]

    def get_edges(valid_vertices, num_edges):
        return [(random.choice(list(valid_vertices)), random.choice(list(valid_vertices))) for i in range(num_edges)]

    edges_list = [get_edges(p, num_random_edges_per_partition) for p in partition]
    full_edge_set = set().union(*edges_list)

    G = nu.vertex_edge_sets_to_graph({i for i in range(num_nodes)}, full_edge_set)

    # Basic structural checks
    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() >= 5
    assert G.number_of_edges() >= 2

    # Partition validity checks
    assert len(partition) >= 2
    assert all(len(group) > 0 for group in partition)
    union = set().union(*partition)
    assert union == set(G.nodes())
    assert sum(len(group) for group in partition) == len(union)

    # Modularity check
    q = nx.community.modularity(G, partition)
    assert q >= 0.95    # Q >= 0.95