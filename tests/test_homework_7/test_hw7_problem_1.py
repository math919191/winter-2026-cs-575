import networkx as nx
from typing import Tuple, Hashable, Set

import network_utilities as nu
import random

def test_hw7_problem_1() -> None:
    """
    Problem 1: Create a graph and a partition of the nodes such that Q = 0.
    Graph must have >= 5 vertices, >= 2 edges, and partition must have >= 2 sets.
    """

    # Build graph
    G: nx.Graph = nx.Graph()

    num_nodes = 60
    edges = [(random.randint(0,num_nodes-1),random.randint(0,num_nodes-1)) for i in range(1000)]

    G = nu.vertex_edge_sets_to_graph({i for i in range(num_nodes)}, set(edges))

    partition = [set(range(num_nodes // 3)),set(range(num_nodes // 3, 2 * num_nodes // 3)),set(range(2 * num_nodes // 3,num_nodes)) ]

    # TODO: Add vertices
 
    # TODO: Add edges

    # TODO: Define partition
    # partition: Tuple[Set[Hashable], ...] = ()

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
    assert abs(q - 0.0) < 0.01  # Q ≈ 0