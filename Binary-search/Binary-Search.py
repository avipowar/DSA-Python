# return thr iddex
# if the element does not exist return -1
 
def BinarySearch(arr , target):
    # indexs of arr
    start = 0
    end = len(arr) -1

    # travels the whole array using while loop
    while(start <= end):

        # find thr  middle element
        mid = (start + end) // 2

        if (target < arr[mid]):
            end = mid - 1
        elif (target > arr[mid]):
            start = mid + 1
        else:
            # ans found
            return mid  

    # ans does not found
    return -1 


arr = [-18, -12, -4, 0, 2, 3, 4, 15, 16, 18, 22, 89, 95]   
target = -4

ans = print(BinarySearch(arr,target))
print(ans)



