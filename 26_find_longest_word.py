# find the longest word in the sentence

def findLongest(sent:str):
    text=sent.split()
    longest_word=""
    for word in text:
        if len(word) > len(longest_word):
            longest_word=word
    
    return f"longest word is {longest_word}"

sentence="Python is a programming languge"
print(findLongest(sentence))


# same for shortest word just change len(word) < len(longest_word) 