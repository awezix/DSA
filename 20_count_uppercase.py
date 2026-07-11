# count uppercase

def countUppercase(text:str):
    count_upper=0
    for char in text:
        if char.isupper():
            count_upper+=1
    return count_upper

text="PytHon"
print(countUppercase(text))

# for lowercase

def countLowercase(text:str):
    count_lower=0
    for char in text:
        if char.islower():
            count_lower+=1
    return count_lower

print(countLowercase(text))
