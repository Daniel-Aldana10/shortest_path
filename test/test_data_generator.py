import random
import unittest
from data import data_generator

class TestGraphSize(unittest.TestCase):
    def test_valid_sizes(self):
        test_sizes = [1, 5, 100]  #
        for size in test_sizes:
            graph_data = data_generator.get_random_graph(size)
            graph = graph_data[0]
            self.assertEqual(len(graph), size)

    def test_size_zero(self):
        graph_data = data_generator.get_random_graph(0)

        self.assertEqual(len(graph_data), 4)
        self.assertEqual(graph_data[0], [])
        self.assertEqual(graph_data[1], -1)
        self.assertEqual(graph_data[2], -1)
        self.assertEqual(graph_data[3], 0)

    def test_path_guarantee(self):
        for _ in range(100):
            size = random.randint(10, 50)
            graph_data = data_generator.get_random_graph(size, ensure_path=True)
            graph, start, goal, _ = graph_data
            self.assertTrue(data_generator.has_path(graph, start, goal))

    def test_valid_edges(self):
        size = 10
        graph_data = data_generator.get_random_graph(size)
        graph = graph_data[0]
        for node in range(size):
            for edge in graph[node]:
                neighbor, weight = edge
                self.assertTrue(0 <= neighbor < size)
                self.assertTrue(weight > 0)

    def test_single_node(self):
        graph_data = data_generator.get_random_graph(1)
        graph, start, goal, _ = graph_data

        self.assertEqual(start, 0)
        self.assertEqual(goal, 0)
        # No debe haber aristas
        self.assertEqual(len(graph[0]), 0)
