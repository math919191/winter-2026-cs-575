import networkx as nx
from typing import Tuple, Hashable, Set

import random
import network_utilities as nu

def test_hw7_problem_3() -> None:
    """
    Problem 3: Create a graph and a partition of the nodes such that Q = -1/2.
    Graph must have >= 5 vertices, >= 2 edges, and partition must have >= 2 sets.
    """

    num_nodes = 60
    partition_size = 20 
    num_random_edges_between_partitions = 45

    partition = [set(range(i,i+partition_size)) for i in range(0,num_nodes,partition_size)]

    def get_edges(valid_vertices_1, valid_vertices_2, num_edges):
        return [(random.choice(list(valid_vertices_1)), random.choice(list(valid_vertices_2))) for i in range(num_edges)]

    i = 0
    edges_list = [
        get_edges(partition[i], partition[i + 1], num_random_edges_between_partitions)]


    full_edge_set = set().union(*edges_list)

    G = nu.vertex_edge_sets_to_graph({i for i in range(num_nodes)}, full_edge_set)

    # Validate structure
    assert isinstance(G, nx.Graph)
    assert G.number_of_nodes() >= 5
    assert G.number_of_edges() >= 2

    # Validate partition
    assert len(partition) >= 2
    assert all(len(group) > 0 for group in partition)
    union = set().union(*partition)
    assert union == set(G.nodes())
    assert sum(len(group) for group in partition) == len(union)

    # Check modularity
    q = nx.community.modularity(G, partition)
    assert abs(q - (-0.5)) < 0.01  # Q ≈ -1/2
