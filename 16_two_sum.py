# Find all pairs whose sum equals a target.allow duplicates

def twosum(arr1:list,target:int)->list:

     # now iterate through loop for two sum
     for i in range(len(arr1)-1):
          for j in range(i+1,len(arr1)):
               if arr1[i] + arr1[j] == target:
                    return i,j
          

array=[12,3,5,6,2]
target=5
print(twosum(array,target))