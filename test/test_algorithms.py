import unittest
from shortest_path import algorithms

class TestShortestPaths(unittest.TestCase):
    def setUp(self):

        self.graph_dijkstra = [
            [(1, 3), (2, 1), (3, 10)],
            [(4, 2)],
            [(4, 4)],
            [(4, 1)],
            []
        ]


        self.graph_bellman = [
            [(1, 4), (2, -1)],
            [(2, -2)],
            []
        ]


        self.graph_bellman_cycle = [
            [(1, 1)],
            [(2, -1)],
            [(0, -1)]
        ]


        self.graph_floyd = [
            [(1, 4), (2, -1)],
            [(2, -2)],
            []
        ]

    def test_dijkstra(self):
        result = algorithms.dijkstra(self.graph_dijkstra, 0)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 3)
        self.assertEqual(result[2], 1)
        self.assertEqual(result[4], 5)

    def test_dijkstra_no_path(self):
        result = algorithms.dijkstra(self.graph_dijkstra, 4)
        self.assertEqual(result[0], float('inf'))

    # Tests para Bellman-Ford
    def test_bellman_ford_without_cycle(self):
        result = algorithms.bellman_ford(self.graph_bellman, 0)
        self.assertEqual(result[2], -1)

    def test_bellman_ford_detects_cycle(self):
        result = algorithms.bellman_ford(self.graph_bellman_cycle, 0)
        self.assertEqual(result, "Negative cycle detected")

    # Tests para Floyd-Warshall
    def test_floyd_warshall_negative_weights(self):
        result = algorithms.floyd_warshall(self.graph_floyd)
        self.assertEqual(result[0][2], -1)

if __name__ == '__main__':
    unittest.main()