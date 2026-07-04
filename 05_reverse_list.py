# reverse list without using built in tools

def rev_arr(arr):
    left=0
    right=len(arr) - 1

    while left < right:
        arr[left],arr[right]=arr[right],arr[left]    #swapping the left and right

        left+=1
        right-=1
    
    return arr



a=[1,23,43,5,56,77,24]
print("original array:",a)
print("reversed array:",rev_arr(a))

