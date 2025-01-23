
def linear(arr, target):
    for i in range(len(arr)):
       if arr[i] == target:
           return i
    return -1
array = [1 ,4,3,5,7]
target = 7
result = linear(array , target)
print(result)





def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage
arr = [23, 1, 56, 8, 15]
target = 8
a = linear_search(arr , target)
print(a)