# Count words in a sentence.

def countWords(sent:str):
    # count=0
    # for words in sent:
    #     if words == " ":
    #         count+=1
    # return count
    
    # if there is space it will count as word so this method in not working

    words=sent.split()   #this will split sentence into list
    return len(words)

sentence="Hii my name is Arsh."
print(countWords(sentence))