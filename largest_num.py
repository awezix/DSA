# finding the largest no. from list without using max()

a=[11,33,5,81,2,4,9,21,40]
       
def largest_no(nums):

    largest=nums[0]    #first start with first element of list
    for num in nums:
        if num > largest:
           largest=num
    
    return largest

print(largest_no(a))