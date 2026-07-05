# Move all negative numbers to the left.
# Move all positive numbers to the right.

def mov_right(no):
    j=0
    for i in range(len(no)):
        if no[i]<0:
            no[i],no[j]=no[j],no[i]
            j+=1
    return no

arr=[1,3,-2,4,-32,67,-3,0,-1,34]
print(mov_right(arr))