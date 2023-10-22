def findmax(arr):
    
    max = arr[0]

    # find the max value
    for i in range(1,len(arr)):

        if (arr[i] > max):
            max = arr[i]

    return max

# declear the aray and calling function
arr = [1,211,3,4,5]
print(findmax(arr))