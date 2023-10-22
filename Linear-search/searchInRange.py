# Search for 3 in range of index[1,4]


# return the index
def SearchInRange(arr,target,start,end):
    # Find the size of aaray
    sizeofArray = len(arr)

    if(sizeofArray == 0):
        return -1

         # run a for loop
    for index in range(start,end+1):
        # check for element every index if it is == target
        if(arr[index] == target):
            return index
            
    # hence the target doesnot found
    return -1


arr = [18,12,-7,3,14,28]
target= 28
start = 0
end = 4


# call the function here
ans = SearchInRange(arr,target,start,end)
print(ans)