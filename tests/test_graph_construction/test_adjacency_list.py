import pytest
import sys
sys.path.insert(0, '/Users/mike/Dropbox/Mac/Documents/Classes/CS 575/Winter 2026/Code/winter-2026-cs-575/src')

import network_utilities as nu
from network_utilities import IllegalGraphRepresentation


class TestAdjacencyListGraphCreationFailures:
    """Negative tests for adjacency list graph creation."""
    
    def test_empty_adjacency_list(self):
        """Test that empty adjacency list raises IllegalGraphRepresentation."""
        expected_error_message: str = "Adjacency list had no vertices"
        
        with pytest.raises(IllegalGraphRepresentation) as exc_info:
            _ = nu.adjacency_list_to_graph(dict())
        
        assert str(exc_info.value) == expected_error_message
    
    def test_missing_edges_undirected_graph(self):
        """Test that asymmetric adjacency list raises IllegalGraphRepresentation."""
        expected_error_message: str = "Adjacency list for undirected graph does not have all required edges"
        
        # Adjacency list where edge 1->2 exists but 2->1 doesn't
        asymmetric_adjacency_list = {1: {2}, 2: set()}
        
        with pytest.raises(IllegalGraphRepresentation) as exc_info:
            _ = nu.adjacency_list_to_graph(asymmetric_adjacency_list)
        
        assert str(exc_info.value) == expected_error_message


class TestAdjacencyListGraphCreationSuccess:
    """Positive tests for adjacency list graph creation."""
    
    def test_three_vertex_undirected_graph(self):
        """Test successful creation of undirected graph from adjacency list."""
        expected_vertex_list = [1, 2, 3]
        expected_edge_set = {(1, 2), (1, 3)}
        
        adjacency_list = {3: {1}, 1: {2, 3}, 2: {1}}
        G = nu.adjacency_list_to_graph(adjacency_list)
        
        # Normalize edges for undirected graph by sorting endpoints
        actual_edge_set = set(tuple(sorted(edge)) for edge in G.edges())
        
        assert expected_vertex_list == sorted(list(G.nodes()))
        assert actual_edge_set == expected_edge_set
    
    def test_three_vertex_directed_graph(self):
        """Test successful creation of directed graph from adjacency list."""
        expected_vertex_list = [1, 2, 3]
        expected_edge_set = {(1, 2), (1, 3), (3, 1), (2, 3)}
        
        adjacency_list = {3: {1}, 1: {2, 3}, 2: {3}}
        G = nu.adjacency_list_to_digraph(adjacency_list)
        
        actual_edge_set = set(tuple(edge) for edge in G.edges())
        
        assert expected_vertex_list == sorted(list(G.nodes()))
        assert actual_edge_set == expected_edge_set
