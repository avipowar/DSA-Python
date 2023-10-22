def FindMax(arr):
    # length of arr
    sizeofArrayRows = len(arr)

    # find max intialyza the valur 
    max = arr[0][0]

    # run a loop in row 
    for rows in range(0,sizeofArrayRows):
        # run a loop in col
        for col in range(0, len(arr[rows])):
            # check maxm 
            if(arr[rows][col] > max):
                max = arr[rows][col]
    return max

# declear the 2d array
arr = [
    [12,-1,-10,14],
    [12111,145,178,2000],
    [-2,-111]
] 
# finction call
ans = FindMax(arr)
print(ans)   