
# Check if an array is a palindrome.

def palindrome(arr):


    left=0
    right=len(arr) - 1

    while left < right:
        if arr[left] != arr[right]:
            return "not palindrome"
        left+=1
        right-=1

arr=[1,2,3,4]
print(palindrome(arr))