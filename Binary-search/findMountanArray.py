# https://leetcode.com/problems/find-in-mountain-array/description/
def FindPeak(arr):
    start = 0
    end = len(arr) - 1

    while(start < end):

        mid = (start+end) // 2

        if(arr[mid] > arr[mid+1]):
            end = mid 
        else:
            start = mid + 1 

    return start                 

def orderAgnosticBS(arr, target, start, end):
    # Check for asending order
    IsAsc = arr[start] < arr[end]
    
    while start <= end:

        mid = (start + end) // 2

        if target == arr[mid]:
            return mid

        if IsAsc:
            
            if arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        else:

            if arr[mid] < target:
                end = mid - 1
            else:
                start = mid + 1

    return -1


def FindMontanArray(arr, target):
    peak = FindPeak(arr)
    start = 0
    end = len(arr) - 1
    first = orderAgnosticBS(arr, target, start, peak)

    if first != -1:
        return first

    return orderAgnosticBS(arr, target, peak+1, end)    


arr = [1, 2, 3, 4, 5, 3, 1]
target = 3

ans = FindMontanArray(arr, target)
print(ans)

