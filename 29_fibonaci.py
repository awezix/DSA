# Fibonacci series

def fib_series(length):
    if length==0:
        return []
    if length==1:
        return [0]
    arr=[0,1]
    for _ in range(2,length):
        arr.append(arr[-1]+arr[-2])
    return arr


n=int(input("enter length of series:"))
print(fib_series(n))