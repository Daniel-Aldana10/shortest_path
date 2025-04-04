import unittest


from shortest_path import algorithms



class TestShortestPaths(unittest.TestCase):
    def setUp(self):
        self.graph_dijkstra = {
            'A': {'B': 3, 'C': 1, 'D': 10},
            'B': {'E': 2},
            'C': {'E': 4},
            'D': {'E': 1},
            'E': {}
        }

        self.graph_bellman = {
            'A': {'B': 4, 'C': -1},
            'B': {'C': -2},
            'C': {}
        }

        self.graph_bellman_negative_cycle = {
            'A': {'B': 1},
            'B': {'C': -1},
            'C': {'A': -1}
        }

        self.graph_floyd_negative = {
            'A': {'B': 4, 'C': -1},
            'B': {'C': -2},
            'C': {}
        }

    # Tests para Dijkstra
    def test_dijkstra(self):
        result = algorithms.dijkstra(self.graph_dijkstra, 'A')
        self.assertEqual(result['A'], 0)
        self.assertEqual(result['B'], 3)
        self.assertEqual(result['C'], 1)
        self.assertEqual(result['E'], 5)

    def test_dijkstra_no_path(self):
        result = algorithms.dijkstra(self.graph_dijkstra, 'E')
        self.assertEqual(result['A'], float('inf'))
    # Tests para Bellman-Ford
    def test_bellman_ford_without_cycle(self):
        result = algorithms.bellman_ford(self.graph_bellman, 'A')
        self.assertEqual(result['C'], 2)

    def test_bellman_ford_with_cycle(self):
        result = algorithms.bellman_ford(self.graph_bellman_negative_cycle, 'A')
        self.assertEqual(result, "There is a negative cycle")

    def test_bellman_ford_without_cycle(self):
        result = algorithms.bellman_ford(self.graph_bellman, 'A')
        self.assertEqual(result['C'], -1)

    def test_floyd_warshall_negative_weights(self):
        result = algorithms.floyd_warshall(self.graph_floyd_negative)
        self.assertEqual(result['A']['C'], -1)


if __name__ == '__main__':
    unittest.main()