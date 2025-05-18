import sys
from data.execution_time_gathering import run_single_source_experiment, run_all_pairs_experiment

import matplotlib.pyplot as plt


def print_results(table, experiment_type):
    """
    Print experiment results in a formatted table.
    
    Args:
        table: Results data from the experiment
        experiment_type: Type of experiment ("single_source" or "all_pairs")
    """
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
                   "Floyd-Warshall (Mem)", "Dijkstra All (Mem)", "Bellman-Ford All (Mem)"]
        print("\n" + "=" * 120)
        print("{:<6} | {:<20} | {:<20} | {:<20} | {:<15} | {:<15} | {:<15}".format(*headers))
        print("-" * 120)
        for row in table:
            print("{:<6} | {:<20.6f} | {:<20.6f} | {:<20.6f} | {:<15.2f} | {:<15.2f} | {:<15.2f}".format(*row))


def plot_results(single_source_data, all_pairs_data):
    """
    Plot experiment results as line graphs.
    
    Args:
        single_source_data: Results from single source experiment
        all_pairs_data: Results from all pairs experiment
    """
    # Plot time comparison for single source algorithms
    plt.figure(figsize=(12, 10))
    
    # Single source execution time chart
    plt.subplot(2, 2, 1)
    sizes_ss = [row[0] for row in single_source_data]
    d_times = [row[1] for row in single_source_data]
    bf_times = [row[2] for row in single_source_data]
    fw_times = [row[3] for row in single_source_data]

    plt.plot(sizes_ss, d_times, 'o-', label='Dijkstra')
    plt.plot(sizes_ss, bf_times, 's-', label='Bellman-Ford')
    plt.plot(sizes_ss, fw_times, '^-', label='Floyd-Warshall')
    plt.xlabel("Graph Size")
    plt.ylabel("Time (seconds)")
    plt.title("Single Source Shortest Path - Time Comparison")
    plt.legend()
    plt.grid(True)
    
    # Single source memory usage chart
    plt.subplot(2, 2, 2)
    d_mems = [row[4] for row in single_source_data]
    bf_mems = [row[5] for row in single_source_data]
    fw_mems = [row[6] for row in single_source_data]
    
    plt.plot(sizes_ss, d_mems, 'o-', label='Dijkstra')
    plt.plot(sizes_ss, bf_mems, 's-', label='Bellman-Ford')
    plt.plot(sizes_ss, fw_mems, '^-', label='Floyd-Warshall')
    plt.xlabel("Graph Size")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("Single Source Shortest Path - Memory Usage")
    plt.legend()
    plt.grid(True)

    # All pairs execution time chart
    plt.subplot(2, 2, 3)
    sizes_ap = [row[0] for row in all_pairs_data]
    fw_times_ap = [row[1] for row in all_pairs_data]
    d_times_ap = [row[2] for row in all_pairs_data]
    bf_times_ap = [row[3] for row in all_pairs_data]

    plt.plot(sizes_ap, fw_times_ap, 'o-', label='Floyd-Warshall')
    plt.plot(sizes_ap, d_times_ap, 's-', label='Dijkstra (All Pairs)')
    plt.plot(sizes_ap, bf_times_ap, '^-', label='Bellman-Ford (All Pairs)')
    plt.xlabel("Graph Size")
    plt.ylabel("Time (seconds)")
    plt.title("All Pairs Shortest Paths - Time Comparison")
    plt.legend()
    plt.grid(True)
    
    # All pairs memory usage chart
    plt.subplot(2, 2, 4)
    fw_mems_ap = [row[4] for row in all_pairs_data]
    d_mems_ap = [row[5] for row in all_pairs_data]  # New data from updated execution_time_gathering
    bf_mems_ap = [row[6] for row in all_pairs_data]  # New data from updated execution_time_gathering
    
    plt.plot(sizes_ap, fw_mems_ap, 'o-', label='Floyd-Warshall')
    plt.plot(sizes_ap, d_mems_ap, 's-', label='Dijkstra (All Pairs)')
    plt.plot(sizes_ap, bf_mems_ap, '^-', label='Bellman-Ford (All Pairs)')
    plt.xlabel("Graph Size")
    plt.ylabel("Memory Usage (bytes)")
    plt.title("All Pairs Shortest Paths - Memory Usage")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()


def run_experiments(min_size=10, max_size=100, step=10, samples=5):
    """
    Run both single source and all pairs experiments.
    
    Args:
        min_size: Minimum graph size
        max_size: Maximum graph size
        step: Size increment
        samples: Number of samples per size
    
    Returns:
        Tuple of (single_source_data, all_pairs_data)
    """
    print(f"Running single source experiment (size {min_size} to {max_size}, step {step}, {samples} samples per size)...")
    single_source_data = run_single_source_experiment(min_size, max_size, step, samples)
    
    # Use smaller sizes for all-pairs experiment as it's much slower
    all_pairs_max = min(max_size, 50)  # Limit to 50 for all-pairs to avoid long wait
    print(f"Running all pairs experiment (size {min_size} to {all_pairs_max}, step {step}, {samples} samples per size)...")
    all_pairs_data = run_all_pairs_experiment(min_size, all_pairs_max, step, samples)
    
    return single_source_data, all_pairs_data


if __name__ == "__main__":
    # Allow command line arguments for experiment parameters
    min_size = 10
    max_size = 100
    step = 10
    samples = 3
    
    # Parse command line arguments if provided
    if len(sys.argv) > 1:
        min_size = int(sys.argv[1])
    if len(sys.argv) > 2:
        max_size = int(sys.argv[2])
    if len(sys.argv) > 3:
        step = int(sys.argv[3])
    if len(sys.argv) > 4:
        samples = int(sys.argv[4])
    
    # Run experiments
    single_source_data, all_pairs_data = run_experiments(min_size, max_size, step, samples)

    # Print and plot results
    print_results(single_source_data, "single_source")
    print_results(all_pairs_data, "all_pairs")
    plot_results(single_source_data, all_pairs_data)
