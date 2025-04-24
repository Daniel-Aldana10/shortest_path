import sys
from data.execution_time_gathering import run_single_source_experiment, run_all_pairs_experiment

import matplotlib.pyplot as plt


def print_results(table, experiment_type):

    if experiment_type == "single_source":
        headers = ["Size", "Dijkstra (Time)", "Bellman-Ford (Time)", "Floyd-Warshall (Time)",
                   "Dijkstra (Mem)", "Bellman-Ford (Mem)", "Floyd-Warshall (Mem)"]
        print("\n" + "=" * 105)
        print("{:<6} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15}".format(*headers))
        print("-" * 105)
        for row in table:
            print("{:<6} | {:<15.6f} | {:<15.6f} | {:<15.6f} | {:<15.2f} | {:<15.2f} | {:<15.2f}".format(*row))

    elif experiment_type == "all_pairs":
        headers = ["Size", "Floyd-Warshall (Time)", "Dijkstra All (Time)", "Bellman-Ford All (Time)",
                   "Floyd-Warshall (Mem)"]
        print("\n" + "=" * 90)
        print("{:<6} | {:<20} | {:<20} | {:<20} | {:<20}".format(*headers))
        print("-" * 90)
        for row in table:
            print("{:<6} | {:<20.6f} | {:<20.6f} | {:<20.6f} | {:<20.2f}".format(*row))

def plot_results(single_source_data, all_pairs_data):
    sizes_ss = [row[0] for row in single_source_data]
    d_times = [row[1] for row in single_source_data]
    bf_times = [row[2] for row in single_source_data]
    fw_times = [row[3] for row in single_source_data]

    plt.figure(figsize=(12, 5))
    plt.plot(sizes_ss, d_times, 'o-', label='Dijkstra (Single Source)')
    plt.plot(sizes_ss, bf_times, 's-', label='Bellman-Ford (Single Source)')
    plt.plot(sizes_ss, fw_times, '^-', label='Floyd-Warshall (Single Source)')
    plt.xlabel("Graph Size")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Times (Single Source)")
    plt.legend()
    plt.grid()
    plt.show()

    sizes_ap = [row[0] for row in all_pairs_data]
    fw_times_ap = [row[1] for row in all_pairs_data]
    d_times_ap = [row[2] for row in all_pairs_data]
    bf_times_ap = [row[3] for row in all_pairs_data]

    plt.figure(figsize=(12, 5))
    plt.plot(sizes_ap, fw_times_ap, 'o-', label='Floyd-Warshall')
    plt.plot(sizes_ap, d_times_ap, 's-', label='Dijkstra (All Pairs)')
    plt.plot(sizes_ap, bf_times_ap, '^-', label='Bellman-Ford (All Pairs)')
    plt.xlabel("Graph Size")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Times  (All Pairs)")
    plt.legend()
    plt.grid()
    plt.show()




if __name__ == "__main__":

    single_source_data = run_single_source_experiment(min_size=10, max_size=100, step=10)
    all_pairs_data = run_all_pairs_experiment(min_size=10, max_size=100, step=10)


    print_results(single_source_data, "single_source")
    print_results(all_pairs_data, "all_pairs")


    plot_results(single_source_data, all_pairs_data)