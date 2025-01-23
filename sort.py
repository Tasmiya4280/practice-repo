unsorted_list = [1, 4, 2, 5, 9, 6, 3, 8, 7]

def bubble_sort(unsorted):
    for i in range(len(unsorted)):  
        swaps = 0
        for j in range(len(unsorted) - 1 - i):  
            if unsorted[j] > unsorted[j + 1]:
               
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
                swaps += 1
        if swaps == 0:  
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
    
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

(insertion_sort(arr))
print(arr)
