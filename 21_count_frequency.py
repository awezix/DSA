# count the frequency of character

def count_frequency(text:str,target):
    count=0
    for char in text.lower():
        if char == target:
            count+=1
    return count

text="programming"
target="p"

print(count_frequency(text,target))