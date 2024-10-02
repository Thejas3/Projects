def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_optimized(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

# Example usage:
arr = [2,1,4,8,6,5,3,7,9,10])
print("Bubble Sort:")
print("Sorted array:", sorted_arr)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

arr_sorted = sorted(arr)
sorted_arr_optimized, comparisons_optimized, swaps_optimized = bubble_sort_optimized(arr_sorted.copy())
print("\nBubble Sort Optimized:")
print("Sorted array:", sorted_arr_optimized)
print("Comparisons:", comparisons_optimized)
print("Swaps:", swaps_optimized)
