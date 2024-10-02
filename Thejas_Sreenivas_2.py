#this part takes the regular bubble sort and allows an array to be sorted in numerical order, ascending. 
def bubble_sort(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                swapped = True
    return array, comparisons, swaps

#this part takes the regular bubble sort and allows it to be optomized so that it will not run through as much comparisions as the regular bubble sort. 
def bubble_sort_optimized(array):
    n = len(array)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
        # If no swaps are made in the first pass, the array is already sorted
        # so now, no further iterations are needed
        if i == 0 and not swapped:
            comparisons += n - 1
            break
    return array, comparisons, swaps

# Exam Inputs:
array= [1,2,3,4,5,6,10,7,8,9]

#prints the stats of the regular bubble sort
sorted_array, comparisons, swaps = bubble_sort(array.copy())
print("Bubble Sort:")
print("Sorted array:", sorted_array)
print("Comparisons:", comparisons)
print("Swaps:", swaps)


#prints the new optimized stats of the bubble sort.
array_sorted = sorted(array)
sorted_array_optimized, comparisons_optimized, swaps_optimized = bubble_sort_optimized(array_sorted.copy())
print("\nBubble Sort Optimized:")
print("Sorted array:", sorted_array_optimized)
print("Comparisons:", comparisons_optimized)
print("Swaps:", swaps_optimized)
