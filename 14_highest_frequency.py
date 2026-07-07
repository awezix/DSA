# Find the element with the highest frequency.

def highest_frequency(arr):
    frequency={}
    max_count=0
    most_frequent=None

    for num in arr:
        if num in frequency:
            frequency[num]+=1

        else:
            frequency[num]=1

        if frequency[num] > max_count:
            max_count=frequency[num]
            most_frequent=num

    return most_frequent,frequency


arr=[1,2,4,5,2,3,6,8,5,6,3,1,1]
print(highest_frequency(arr))