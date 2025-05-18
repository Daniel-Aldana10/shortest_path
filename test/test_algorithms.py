import unittest
from shortest_path import algorithms


class TestShortestPaths(unittest.TestCase):
    def setUp(self):
        # Graph for testing Dijkstra's algorithm (non-negative weights)
        self.graph_dijkstra = [
            [(1, 3), (2, 1), (3, 10)],
            [(4, 2)],
            [(4, 4)],
            [(4, 1)],
            []
        ]

        # Graph for testing Bellman-Ford algorithm (with negative weights)
        self.graph_bellman = [
            [(1, 4), (2, -1)],
            [(2, -2)],
            []
        ]

        # Graph with a negative cycle for testing
        self.graph_bellman_cycle = [
            [(1, 1)],
            [(2, -1)],
            [(0, -1)]
        ]

        # Generic graph for testing all algorithms
        self.graph_generic = [
            [(1, 4), (2, 2), (3, 7)],
            [(0, 4), (2, 1), (4, 5)],
            [(0, 2), (1, 1), (3, 3), (4, 8)],
            [(0, 7), (2, 3), (4, 2)],
            [(1, 5), (2, 8), (3, 2)]
        ]

    def test_dijkstra_single_destination(self):
        # Test Dijkstra with specific start and end points
        result = algorithms.dijkstra(self.graph_dijkstra, 0, 4)
        self.assertEqual(result, 5)

    def test_dijkstra_no_path(self):
        # Test when there is no path
        result = algorithms.dijkstra(self.graph_dijkstra, 4, 0)
        self.assertEqual(result, float('inf'))

    def test_bellman_ford_negative_weights(self):
        # Test Bellman-Ford with negative weights
        result = algorithms.bellman_ford(self.graph_bellman, 0, 2)
        self.assertEqual(result, -1)

    def test_bellman_ford_detects_cycle(self):
        # Test that Bellman-Ford detects negative cycles
        result = algorithms.bellman_ford(self.graph_bellman_cycle, 0)
        self.assertEqual(result, "Negative cycle detected")

    def test_floyd_warshall_single_pair(self):
        # Test Floyd-Warshall between specific points
        result = algorithms.floyd_warshall(self.graph_bellman, 0, 2)
        self.assertEqual(result, -1)

    def test_all_algorithms_same_result(self):
        # Test that all algorithms yield the same result on the same graph
        start, end = 0, 4

        dijkstra_result = algorithms.dijkstra(self.graph_generic, start, end)
        bellman_ford_result = algorithms.bellman_ford(self.graph_generic, start, end)
        floyd_warshall_result = algorithms.floyd_warshall(self.graph_generic, start, end)

        self.assertEqual(dijkstra_result, bellman_ford_result)
        self.assertEqual(dijkstra_result, floyd_warshall_result)
        self.assertEqual(bellman_ford_result, floyd_warshall_result)

    def test_original_outputs(self):
        # Test that the original output formats still work
        # Dijkstra and Bellman-Ford returning all distances
        dijkstra_distances = algorithms.dijkstra(self.graph_dijkstra, 0)
        self.assertEqual(dijkstra_distances[0], 0)
        self.assertEqual(dijkstra_distances[1], 3)
        self.assertEqual(dijkstra_distances[2], 1)
        self.assertEqual(dijkstra_distances[4], 5)

        # Floyd-Warshall returning the distance matrix
        fw_matrix = algorithms.floyd_warshall(self.graph_bellman)
        self.assertEqual(fw_matrix[0][2], -1)


if __name__ == '__main__':
    unittest.main()