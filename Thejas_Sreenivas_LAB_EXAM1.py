#the regular bubble sort algorithm which allows you to be able to sort an array in numerical order for this example. This does not take the time it might take and power it 
#might take to do this in a larger scale. 

def bubble_sort(arr):
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


#The optomized version of this code allows you to sort an array in numerical order, but this time it will take into consideration how many time it swaps and comparisions and
#will try to potomize it. 
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

# Exam Inputs:
arr = [1,2,3,4,5,6,10,7,8,9]

#prints out the stats for the regular bubble sort
sorted_arr, comparisons, swaps = bubble_sort(arr.copy())
print("Bubble Sort:")
print("Sorted array:", sorted_arr)
print("Comparisons:", comparisons)
print("Swaps:", swaps)

#Prints the new optomized bubble sort, to be able to compare it.
arr_sorted = sorted(arr)
sorted_arr_optimized, comparisons_optimized, swaps_optimized = bubble_sort_optimized(arr_sorted.copy())
print("\nBubble Sort Optimized:")
print("Sorted array:", sorted_arr_optimized)
print("Comparisons:", comparisons_optimized)
print("Swaps:", swaps_optimized)
