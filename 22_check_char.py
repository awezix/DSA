# Check if a character exists in the string.

def checkChar(text:str,char):
    
    # lowercase the target and text
    target=char.lower()
    for i in text.lower():
        if i==target:
            return "Character Exist"
        else:
            return "Character Not Exist"

text="python"
char="P"

print(checkChar(text,char))