# find the smallest num from the list without using min()

def smallest(li):
    smallest=li[0]

    for i in li:
        if i<smallest:
            smallest=i
        
    return smallest

lis=[90,45,20,2,100,34,45,22]
print(smallest(lis))

