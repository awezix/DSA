# Count even numbers

def count_even(no):
    
    count=0
    for n in no:
        if n % 2 == 0:
            count+=1
    return count

array=[1,2,3,4,5,6,7,8,10]
print(count_even(array))
    

