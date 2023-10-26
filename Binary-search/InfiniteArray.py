# https://www.geeksforgeeks.org/find-position-element-sorted-array-infinite-numbers/

# return the index
def BinarySearch(arr, target, start, end):

    while(start <= end):
        
        mid = (start + end) // 2

        if(arr[mid] > target):
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            return mid     
    return -1               

# Pass the array infinite numbers
def ans(arr, target):
    # First find the range
    # first start with box size 2
    start = 0
    end = 1

    while(target > arr[end]):
        # start value updated
        temp = end + 1
        # end value updated
        # end - (start - 1) => end - start + 1
        # double the box value
        # end = privious end + sizeofbox*2 
        end = end + (end - start + 1) * 2
        start = temp

    return BinarySearch(arr, target, start, end)

arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 170]
target = 170

resulet = ans(arr, target) 
print(resulet)

