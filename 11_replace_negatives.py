# Replace all negative numbers with 0.

def replace_neg(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i]=0
    return arr

arr=[1,3,-2,4,-32,67,-3,0,-1,34]
print(replace_neg(arr))