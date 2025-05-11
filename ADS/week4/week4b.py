import random
import time
import sys

sys.setrecursionlimit(10000)  # Increase recursion depth for large inputs

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        # Merge step
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Function to measure execution time
def measure_time(arr):
    start = time.time()
    merge_sort(arr)
    end = time.time()
    return end - start

# Function to generate datasets
def generate_datasets(size):
    average_case = [random.randint(1, size) for _ in range(size)]
    best_case = sorted(average_case.copy())      # Already sorted input
    worst_case = sorted(average_case.copy(), reverse=True)  # Reverse sorted input
    return average_case, best_case, worst_case

# Sizes for testing
sizes = [1000, 2000, 5000, 10000, 20000, 50000]

# Run tests and print results
print("Merge Sort Execution Time Analysis")
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
