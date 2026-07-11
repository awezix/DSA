# reverse string 

def reverse(text:str):
    reversed=""
    for i in text:
        reversed= i+reversed
    return reversed

text="Python is a language"

print(reverse(text))