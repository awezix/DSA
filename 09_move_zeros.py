# Move all zeros to the end without using another array.

# arr=[2,3,0,78,0,5,75,34,0,23,44,0,21]
# output:[2, 3, 78, 5, 75, 34, 23, 44, 21, 0, 0, 0, 0]

def move_zeros(arr):
    x=0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[x],arr[i]=arr[i],arr[x]    #swap the non zero element with x 
            x+=1
    return arr

arr=[2,3,0,78,0,5,75,34,0,23,44,0,21]
print(move_zeros(arr))
   

def zeros_begin(arr):
    j=0
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    return arr

arr1=[2,3,0,78,0,5,75,34,0,23,44,0,21]
print(zeros_begin(arr1))  #but the order changes




