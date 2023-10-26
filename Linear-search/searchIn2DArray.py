def SearchIn2DArray(arr, target):

    sizeofArrayRows = len(arr)

    # first i loop travels on row 
    for row in range(0,sizeofArrayRows):

        # secound c loop travels on col
        for col in range(0,len(arr[row])):
            # comapre the elemnet with target element
            if arr[row][col] == target:
                # create array and return  
                return [row,col]
    # elemnet does not found return -1 -1
    return [-1,-1]
# Create 2D Array 
arr = [
    [1,2,3,4],
    [5,6,7],
    [8,9,10,11,12]
]  
# print(arr[0][0])
# target element you find
target = 6
# creat ans array store the ans will be function return
ans = SearchIn2DArray(arr,target)
print(ans)