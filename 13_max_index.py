# Find the index of the maximum element.

def max_index(arr):
    max_ind=0
    for i in range(len(arr)):
        if arr[i] > arr[max_ind]:
            max_ind=i

    return max_ind

arr=[12,45,32,11,78,98,45,0]

print(max_index(arr))

# index of minimum element

def min_index(arr):
    min_index=0
    for i in range(len(arr)):
        if arr[i]<arr[min_index]:
            min_index=i

    return min_index

print(min_index(arr))