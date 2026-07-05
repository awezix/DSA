# Find the second largest element.

def sec_largst(arr):
   largest=float("-inf")
   s_largest=float("-inf")

   for i in arr:
      if i > largest:
         s_largest=largest
         largest=i

      elif i > s_largest and i != largest:
         s_largest=i
        
   return s_largest


arr=[21,-23,12,54,97,68,9,23,10]
print(sec_largst(arr))

