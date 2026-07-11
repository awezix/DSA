# count the vowels

def countVowels(text:str):
    vowels=['a','e','i','o','u']
    vowels_count=0

    for i in text:
        if i in vowels:
            vowels_count+=1
        
    return vowels_count
    
        
text="programming"
print(countVowels(text))