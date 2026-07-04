
# Print all even elements.
# Print all odd elements.

def odd(arr):
    odd=[]
    for i in arr:
        if i % 2 != 0:
            odd.append(i)
    return odd

array=[1,2,3,4,5,6,7,8,91,2,33,45,44]
print(odd(array))

# same for even elements just change (if i % 2 == 0)