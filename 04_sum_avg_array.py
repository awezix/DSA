# calculate the sum of element of a list

def cal_sum(li):
    sum=0
    for i in li:
        sum +=i
    return sum

array=[1,2,3,4,5,33]
print(cal_sum(array))

# calculate average of all element in the list

def cal_avg(li):
    sum=0
    for i in li:
        sum+=i
    
    avg=sum/len(li)
    return avg

arr=[1,2,3,4,52,33]
print(cal_avg(arr))