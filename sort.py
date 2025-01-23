unsorted_list = [1, 4, 2, 5, 9, 6, 3, 8, 7]

def bubble_sort(unsorted):
    for i in range(len(unsorted)):  # Outer loop to ensure all passes
        swaps = 0
        for j in range(len(unsorted) - 1 - i):  # Reduce comparisons with each pass
            if unsorted[j] > unsorted[j + 1]:
                # Swap elements
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swaps += 1
        if swaps == 0:  # If no swaps, the list is sorted
            break
    return unsorted

fun = bubble_sort(unsorted_list)
print(fun)


quick_list = [7, 3 ,5,2,8,9,10]

def quick_sort(unsorted):
    if len(unsorted)<+1:
        return  unsorted
    else:
        pivot = unsorted[0]
        below_pivot = [x for x in unsorted [1:] if  x <= pivot]
        above_pivot = [x for x in unsorted [1:] if x >= pivot]
        return  quick_sort(below_pivot)+ [pivot] + quick_sort(above_pivot)

result = quick_sort(quick_list)
print(result)



arr=[23,1,56,8]
def insertion_sort(unsorted):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be compared
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at the correct position
        arr[j + 1] = key

(insertion_sort(arr))
print(arr)