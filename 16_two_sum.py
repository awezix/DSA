# Find all pairs whose sum equals a target.

def twosum(arr:list,target:int):
     first=0

     for i in range(len(arr)):
          for j in range(i+1,len(arr)):
               if arr[j] + arr[i] == target:
                    return i,j

arr=[1,3,2,7]
print(twosum(arr,8))