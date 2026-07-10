# Find the median of two sorted array
# duplicates are allowed
# leetcode Array 4th problem

def medianOfTwoArray(arr1:list,arr2:list):
    # first merged the array and then sort
    merged=arr1+arr2
    merged.sort()

    length=len(merged)
    mid=length // 2

    if length % 2 != 0:
        return merged[mid]
    
    else:
        return float((merged[mid-1]+merged[mid])/2)
    

ar1=[1,-4,3]
ar2=[2,7,5,9]
print(medianOfTwoArray(ar1,ar2))
