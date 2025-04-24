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

            tracemalloc.start()
            t_start = time.perf_counter()
            d_dist = dijkstra(graph, start)[goal]
            d_time = time.perf_counter() - t_start
            d_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            tracemalloc.start()
            t_start = time.perf_counter()
            bf_dist = bellman_ford(graph, start)[goal]
            bf_time = time.perf_counter() - t_start
            bf_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            tracemalloc.start()
            t_start = time.perf_counter()
            fw_matrix = floyd_warshall(graph)
            fw_time = time.perf_counter() - t_start
            fw_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()
            fw_dist = fw_matrix[start][goal]
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
        fw_times, d_times, bf_times = [], [], []
        fw_mems = []

        for _ in range(samples):
            graph = get_random_graph(size, ensure_path=True)[0]

            tracemalloc.start()
            t_start = time.perf_counter()
            fw_matrix = floyd_warshall(graph)
            fw_time = time.perf_counter() - t_start
            fw_mem = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            d_total_time = 0
            for start in range(size):
                t_start = time.perf_counter()
                dijkstra(graph, start)
                d_total_time += time.perf_counter() - t_start

            bf_total_time = 0
            for start in range(size):
                t_start = time.perf_counter()
                bellman_ford(graph, start)
                bf_total_time += time.perf_counter() - t_start

            fw_times.append(fw_time)
            d_times.append(d_total_time)
            bf_times.append(bf_total_time)
            fw_mems.append(fw_mem)

        results.append([
            size,
            sorted(fw_times)[len(fw_times) // 2],
            sorted(d_times)[len(d_times) // 2],
            sorted(bf_times)[len(bf_times) // 2],
            sorted(fw_mems)[len(fw_mems) // 2],
        ])
    return results