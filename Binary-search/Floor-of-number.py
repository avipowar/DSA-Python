# Floor of a number
# greatest number less than equal to target
def FloorOfNumber(arr, target):

# target is bigger than array element
    if(target  > arr[len(arr)-1]):
        return -1

    start = 0
    end = len(arr)

    while(start <= end):

        mid = (start + end) //2

        if(arr[mid] == target):
            return arr[mid]
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    # number not found return the end becuase it is greates smallest number 
    return arr[end] 

arr = [2, 3, 5, 9, 14, 16, 18]
target = 19
ans = FloorOfNumber(arr,target)
print(ans)
