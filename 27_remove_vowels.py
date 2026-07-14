# remove the vowels

def removeVowels(text:str):

    vowels=['a','e','i','o','u','A','E','I','O','U']
    result=""
    for i in text:
        if i not in vowels:
            result+=i
    
    return result

text="python language"
print(removeVowels(text))