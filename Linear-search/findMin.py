# Find the minimul element in the given array

def FindMin(arr):
    # find lenght of arr
    sizeofArray = len(arr)

    if(sizeofArray == 1):
        return arr[0]

    min = arr[0]
    # run a loop 
    for i in range(1,sizeofArray):
       # find min 
        if(arr[i] < min):
            min = arr[i]
    return min



arr = [18,12,-7,3,14,-9]
# call the function and print
print(FindMin(arr))