"""
Tests for creating graphs from adjacency matrices.

This module demonstrates testing patterns for the adjacency matrix graph creation utilities.
"""

import sys
from pathlib import Path

import numpy as np
import pytest

# Add src/ to Python path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from network_utilities import IllegalGraphRepresentation
import network_utilities as nu


class TestAdjacencyMatrixGraphCreationFailures:
    """Negative tests: adjacency matrices that should raise errors."""

    def test_empty_adjacency_matrix(self) -> None:
        """Test that an empty adjacency matrix raises IllegalGraphRepresentation."""
        with pytest.raises(IllegalGraphRepresentation) as exc_info:
            _ = nu.adjacency_matrix_to_graph(np.array([]))

        assert str(exc_info.value) == "Adjacency matrix had no vertices"

    def test_asymmetric_adjacency_matrix_undirected_graph(self) -> None:
        """
        Test that an asymmetric adjacency matrix raises an error for undirected graphs.

        For undirected graphs, if A[i][j] = 1, then A[j][i] must also be 1.
        """
        asymmetric_matrix = np.array([[0, 1], [0, 0]])
        with pytest.raises(IllegalGraphRepresentation) as exc_info:
            _ = nu.adjacency_matrix_to_graph(asymmetric_matrix)

        assert str(exc_info.value) == "Adjacency matrix is not symmetric"


class TestAdjacencyMatrixGraphCreationSuccess:
    """Positive tests: adjacency matrices that should successfully create graphs."""

    def test_symmetric_adjacency_matrix_undirected_graph(self) -> None:
        """
        Test that a symmetric adjacency matrix creates an undirected graph correctly.

        The matrix:
        [[0, 1, 1],
         [1, 0, 0],
         [1, 0, 0]]

        Represents vertices {0, 1, 2} with edges {(0,1), (0,2)}.
        """
        # Symmetric adjacency matrix (undirected graph)
        A = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 0]])

        # Verify symmetry
        assert np.array_equal(A, A.T), "Matrix should be symmetric for undirected graphs"

        # Create graph
        G = nu.adjacency_matrix_to_graph(A)

        # Verify vertices
        expected_vertices = {0, 1, 2}
        assert set(G.nodes()) == expected_vertices

        # Verify edges (normalized for undirected graph)
        expected_edges = {(0, 1), (0, 2)}
        actual_edges = set(tuple(sorted(edge)) for edge in G.edges())
        assert actual_edges == expected_edges

    def test_asymmetric_adjacency_matrix_directed_graph(self) -> None:
        """
        Test that an asymmetric adjacency matrix creates a valid directed graph.

        For directed graphs, asymmetry is allowed. A[i][j] = 1 means edge i→j.

        The matrix:
        [[0, 1, 1],
         [0, 0, 1],
         [0, 1, 0]]

        Represents vertices {0, 1, 2} with directed edges {0→1, 0→2, 1→2, 2→1}.
        """
        # Asymmetric adjacency matrix (directed graph is fine with this)
        A = np.array([[0, 1, 1], [0, 0, 1], [0, 1, 0]])

        # Verify asymmetry
        assert not np.array_equal(A, A.T), "Matrix is asymmetric (valid for directed graphs)"

        # Create directed graph
        G = nu.adjacency_matrix_to_digraph(A)

        # Verify vertices
        expected_vertices = {0, 1, 2}
        assert set(G.nodes()) == expected_vertices

        # Verify edges (no normalization needed for directed graphs)
        expected_edges = {(0, 1), (0, 2), (1, 2), (2, 1)}
        actual_edges = set(G.edges())
        assert actual_edges == expected_edges
