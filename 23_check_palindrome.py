# check whether the string is palindrome or not

def checkPalindrome(text:str):

    string=text.lower()
    # first reverse the string then compare it with given string
    reversed=""

    for char in string:
        reversed=char+reversed
    
    if reversed == string:
        return "The given string is palindrome"
    else:
        return "The given string is not palindrome"
    
text="Racecar"
print(checkPalindrome(text))