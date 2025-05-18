import random
import unittest
from data import data_generator

class TestGraphGenerator(unittest.TestCase):
    def test_valid_sizes(self):
        """Test that graphs of different sizes are generated correctly."""
        test_sizes = [1, 5, 100]
        for size in test_sizes:
            graph_data = data_generator.get_random_graph(size)
            graph = graph_data[0]
            self.assertEqual(len(graph), size)

    def test_size_zero(self):
        """Test that a graph of size 0 returns the expected default values."""
        graph_data = data_generator.get_random_graph(0)

        self.assertEqual(len(graph_data), 4)
        self.assertEqual(graph_data[0], [])
        self.assertEqual(graph_data[1], -1)
        self.assertEqual(graph_data[2], -1)
        self.assertEqual(graph_data[3], 0)

    def test_path_guarantee(self):
        """Test that a path exists between start and goal when ensure_path is True."""
        for _ in range(20):  # Reduced to 20 iterations for faster testing
            size = random.randint(10, 30)
            graph_data = data_generator.get_random_graph(size, ensure_path=True)
            graph, start, goal, _ = graph_data
            self.assertTrue(data_generator.has_path(graph, start, goal))

    def test_valid_edges(self):
        """Test that all edges have valid targets and positive weights."""
        size = 10
        graph_data = data_generator.get_random_graph(size)
        graph = graph_data[0]
        for node in range(size):
            for neighbor, weight in graph[node]:
                self.assertTrue(0 <= neighbor < size)
                self.assertTrue(weight > 0)

    def test_single_node(self):
        """Test that a graph with a single node has expected properties."""
        graph_data = data_generator.get_random_graph(1)
        graph, start, goal, _ = graph_data

        self.assertEqual(start, 0)
        self.assertEqual(goal, 0)
        # A single node graph shouldn't have any edges
        self.assertEqual(len(graph[0]), 0)
        
    def test_add_path_function(self):
        """Test that the add_path function creates a valid path."""
        size = 10
        graph = [[] for _ in range(size)]
        start, end = 0, size - 1
        
        # Add a path and verify it exists
        data_generator.add_path(graph, start, end, 100)
        self.assertTrue(data_generator.has_path(graph, start, end))
        
    def test_graph_representation(self):
        """Test that the graph is represented consistently as tuples in adjacency list."""
        size = 5
        graph_data = data_generator.get_random_graph(size)
        graph = graph_data[0]
        
        for node in range(size):
            for edge in graph[node]:
                # Each edge should be a tuple or list of (target, weight)
                self.assertEqual(len(edge), 2)
                neighbor, weight = edge
                self.assertTrue(isinstance(neighbor, int))
                self.assertTrue(isinstance(weight, int))

if __name__ == '__main__':
    unittest.main()
