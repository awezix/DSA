# Find the first repeating character.

def findChar(text:str):
    seen=set()

    for char in text:
        if char in seen:
            return char
        seen.add(char)
    
    return "no repeating character"

text="programming"
print(findChar(text))