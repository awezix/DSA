# count the vowels

def countVowels(text:str):
    vowels=['a','e','i','o','u']
    vowels_count=0

    for i in text.lower():
        if i in vowels:
            vowels_count+=1
        
    return vowels_count
    
        
text="programming"
print(countVowels(text))

# for consonants

def consonantsCount(text:str):
    vowels=['a','e','i','o','u']
    consonants_counts=0

    for i in text.lower():
        if i.isalpha() and i not in vowels:
            consonants_counts+=1
    return consonants_counts

print(consonantsCount(text))

