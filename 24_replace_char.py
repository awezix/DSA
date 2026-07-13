# Replace one character with another.

def replaceChar(text:str,old_char:str,new_char:str):
    result=""
    for i in text.lower():
        if i == old_char:
            result+=new_char
        else:
            result+=i
    return result

text="programming"

print(replaceChar(text,"m","X"))