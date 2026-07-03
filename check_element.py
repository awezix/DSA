# Check if an element exists in the array.

def check_element(el):

    array=[1,23,4,24,67,23,9,36,9,80,93,57]
    for i in array:
        if i == el:
            print("element is present")
            return
    print("element not found")

elem=int(input("enter element:"))
check_element(elem)