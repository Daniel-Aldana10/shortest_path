import time
import tracemalloc
from data.data_generator import get_random_graph
from shortest_path.algorithms import dijkstra, bellman_ford, floyd_warshall

def run_single_source_experiment(min_size=10, max_size=100, step=10, samples=5):

    results = []
    for size in range(min_size, max_size + 1, step):
        print(f"Testing size (single source): {size}")
        d_times, bf_times, fw_times = [], [], []
        d_mems, bf_mems, fw_mems = [], [], []

        for _ in range(samples):
            graph_data = get_random_graph(size, ensure_path=True)
            graph, start, goal, _ = graph_data

            # Dijkstra's algorithm
            tracemalloc.start()
            t_start = time.perf_counter()
            d_dist = dijkstra(graph, start, goal)
            d_time = time.perf_counter() - t_start
            d_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            # Bellman-Ford algorithm
            tracemalloc.start()
            t_start = time.perf_counter()
            bf_dist = bellman_ford(graph, start, goal)
            bf_time = time.perf_counter() - t_start
            bf_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            # Floyd-Warshall algorithm
            tracemalloc.start()
            t_start = time.perf_counter()
            fw_dist = floyd_warshall(graph, start, goal)
            fw_time = time.perf_counter() - t_start
            fw_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()


            assert d_dist == bf_dist == fw_dist, "Discrepancy in distances!"

            d_times.append(d_time)
            bf_times.append(bf_time)
            fw_times.append(fw_time)
            d_mems.append(d_mem)
            bf_mems.append(bf_mem)
            fw_mems.append(fw_mem)

        results.append([
            size,
            sorted(d_times)[len(d_times) // 2],
            sorted(bf_times)[len(bf_times) // 2],
            sorted(fw_times)[len(fw_times) // 2],
            sorted(d_mems)[len(d_mems) // 2],
            sorted(bf_mems)[len(bf_mems) // 2],
            sorted(fw_mems)[len(fw_mems) // 2],
        ])
    return results


def run_all_pairs_experiment(min_size=10, max_size=50, step=10, samples=3):

    results = []
    for size in range(min_size, max_size + 1, step):
        print(f"Testing size (all pairs): {size}")
        fw_times, d_all_times, bf_all_times = [], [], []
        fw_mems, d_all_mems, bf_all_mems = [], [], []

        for _ in range(samples):
            graph = get_random_graph(size, ensure_path=True)[0]

            # Floyd-Warshall (naturally calculates all pairs)
            tracemalloc.start()
            t_start = time.perf_counter()
            fw_matrix = floyd_warshall(graph)  # No start/end to get full matrix
            fw_time = time.perf_counter() - t_start
            fw_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            # Calculate all pairs with Dijkstra by running it from each node
            tracemalloc.start()
            t_start = time.perf_counter()
            d_result = []
            for start in range(size):
                d_result.append(dijkstra(graph, start))  # Get all distances from start
            d_all_time = time.perf_counter() - t_start
            d_all_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            # Calculate all pairs with Bellman-Ford by running it from each node
            tracemalloc.start()
            t_start = time.perf_counter()
            bf_result = []
            for start in range(size):
                bf_result.append(bellman_ford(graph, start))  # Get all distances from start
            bf_all_time = time.perf_counter() - t_start
            bf_all_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            # Verify some random pairs to ensure consistency
            for _ in range(5):  # Check 5 random pairs
                start = size // 2  # Consistent source for simplicity
                end = size // 4    # Consistent target for simplicity
                
                # Convert results to comparable formats
                if isinstance(bf_result[start], str):  # Skip if negative cycle detected
                    break
                    
                d_dist = d_result[start][end]
                bf_dist = bf_result[start][end]
                fw_dist = fw_matrix[start][end]
                
                assert d_dist == bf_dist == fw_dist, f"Discrepancy in distances: {d_dist}, {bf_dist}, {fw_dist}"

            fw_times.append(fw_time)
            d_all_times.append(d_all_time)
            bf_all_times.append(bf_all_time)
            fw_mems.append(fw_mem)
            d_all_mems.append(d_all_mem)
            bf_all_mems.append(bf_all_mem)

        results.append([
            size,
            sorted(fw_times)[len(fw_times) // 2],
            sorted(d_all_times)[len(d_all_times) // 2],
            sorted(bf_all_times)[len(bf_all_times) // 2],
            sorted(fw_mems)[len(fw_mems) // 2],
            sorted(d_all_mems)[len(d_all_mems) // 2],
            sorted(bf_all_mems)[len(bf_all_mems) // 2],
        ])
    return results
