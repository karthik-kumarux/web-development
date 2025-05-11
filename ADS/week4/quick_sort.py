import random
import time
import sys

sys.setrecursionlimit(10000)  # Increase recursion depth if needed (be cautious)

# Quick Sort implementation with Random Pivot
def quick_sort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap random pivot to end
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Function to measure execution time
def measure_time(arr):
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    end = time.time()
    return end - start

# Function to generate datasets
def generate_datasets(size):
    average_case = [random.randint(1, size) for _ in range(size)]  # Random
    best_case = average_case.copy()  # Random pivoting makes best & avg same
    worst_case = sorted(average_case.copy())  # Even if sorted, random pivot avoids worst case
    return average_case, best_case, worst_case

# Sizes for testing
sizes = [1000, 2000, 5000, 10000, 20000, 50000]

# Run tests and print results
print("Quick Sort (Random Pivot) Execution Time Analysis")
print("-----------------------------------")
for size in sizes:
    avg_case, best_case, worst_case = generate_datasets(size)

    time_avg = measure_time(avg_case.copy())
    time_best = measure_time(best_case.copy())
    time_worst = measure_time(worst_case.copy())

    print(f"Input Size: {size}")
    print(f"  Average Case: {time_avg:.5f} seconds")
    print(f"  Best Case:    {time_best:.5f} seconds")
    print(f"  Worst Case:   {time_worst:.5f} seconds")
    print("-----------------------------------")
