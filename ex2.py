import timeit
import random
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)


def bubble_sort(arr):
    n = len(arr)
    for a in range(n):
        swapped = False
        for b in range(0, n-a-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def generate_data(size):
    arr = [random.randint(1, 10000) for _ in range(size)]
    sorted_arr = sorted(arr)  
    reverse_sorted_arr = sorted(arr, reverse=True)  
    return arr, sorted_arr, reverse_sorted_arr


sizes = [10, 50, 100, 200, 300, 400, 500]  
scenarios = ["Average", "Best", "Worst"]

for scenario in scenarios:
    bubble_times = []
    quick_times = []

    for size in sizes:
        arr, sorted_arr, reverse_sorted_arr = generate_data(size)

        if scenario == "Average":
            bubble_time = timeit.timeit(lambda: bubble_sort(arr.copy()), number=1)
            quick_time = timeit.timeit(lambda: quick_sort(arr.copy()), number=1)
        elif scenario == "Best":
            bubble_time = timeit.timeit(lambda: bubble_sort(sorted_arr.copy()), number=1)
            quick_time = timeit.timeit(lambda: quick_sort(sorted_arr.copy()), number=1)
        elif scenario == "Worst":
            bubble_time = timeit.timeit(lambda: bubble_sort(reverse_sorted_arr.copy()), number=1)
            quick_time = timeit.timeit(lambda: quick_sort(reverse_sorted_arr.copy()), number=1)

        bubble_times.append(bubble_time)
        quick_times.append(quick_time)

    
    plt.figure()
    plt.plot(sizes, bubble_times, label='Bubble Sort', marker='o')
    plt.plot(sizes, quick_times, label='Quick Sort', marker='s')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.title(f'Performance Comparison of Bubble Sort and Quick Sort - {scenario} Case')
    plt.legend()
    plt.grid(True)
    plt.show()
    
