# Count positive, negative, and zero values.

def count(ar):
    positive=0
    negative=0
    zero=0
    for i in ar:
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            zero+=1
    return positive,negative,zero

arr=[1,2,3,4,-56,0,7,-4,-24,64,0,43,-21,0]
print("length",len(arr))

positive,negative,zero=count(arr)
print("positives",positive)
print("negatives",negative)
print("zeros",zero)
