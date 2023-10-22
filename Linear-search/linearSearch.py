# Search in thr array: return the index if item find
# Otherwise if item not foung return -1

# return the element
def Linear_Search2(arr,target):
    # Find the size of aaray
    sizeofArray = len(arr) 

    if(sizeofArray == 0):
        return -1

         # run a for loop
    for index in range(sizeofArray):
        # check for element every index if it is == target
        if(arr[index] == target):
            return arr[index]
    # hence the target doesnot found
    return -1



# return the index
def Linear_Search(arr,target):
    # Find the size of aaray
    sizeofArray = len(arr)

    if(sizeofArray == 0):
        return -1

         # run a for loop
    for index in range(sizeofArray):
        # check for element every index if it is == target
        if(arr[index] == target):
            return index
            
    # hence the target doesnot found
    return -1


arr = [13,32,42,16,19]
target= 19

# call the function here
result = Linear_Search(arr,target)
ans = Linear_Search2(arr,target)
print(ans)

# if result != -1:
#     print("Element {target} found at index " ,result)
# else:
#     print("Element {target} not found in the list. ", result)
