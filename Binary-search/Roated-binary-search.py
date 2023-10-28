# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1085955853/
'''
# with duplicate find pivot
def FindPivotWithDuplicate(arr, start, end):

    while start <= end:

        mid = (start + end) // 2
        # if mid > end mid+1 are out of index
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        # if start start > mid mid id out of range
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1

        # if if element are middle start end is equal then the skip the duplicates
        if arr[mid] == arr[start] and arr[mid] == arr[end]:
            # skip the dupliactes
            # Note : if the start and end any one is pivot 
            # check if first start is pivot
            if arr[start] > arr[start+1]:
                return start
            start += 1

            # check end is pivot
            if arr[end] < arr[end-1]:
                return end  - 1
            end -= 1

        # left side is sorted so my pivot is shouldbr right side
        elif arr[start] < arr[mid] or arr[start] == arr[mid] and arr[mid] > arr[end]:
            start = mid + 1 
        else:
            end = mid - 1    

    return -1

'''

# no duplictte element used here
def BinarySearch(arr, start, end, target):

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

def FindPivot(arr, start, end):

    while start <= end:

        mid = (start + end) // 2
        # if mid > end mid+1 are out of index
        if mid < end and arr[mid] > arr[mid + 1]:
            return mid
        # if start start > mid mid id out of range
        elif mid > start and arr[mid] < arr[mid - 1]:
            return mid - 1

        # Search of left side
        elif arr[mid] <= arr[start]:
            end = mid - 1

        else:
            # Search on right side
            start = mid + 1
    return -1

def RoatedBS(arr, target):
    # In Rotated BS, first find the pivot
    Pivot = FindPivot(arr, 0, len(arr) - 1)
    print(Pivot)

    # If you did not find a pivot, means array is sorted; apply simple binary search
    if Pivot == -1:
        return BinarySearch(arr, 0, len(arr) - 1, target)

    # If Pivot is found, you have two ascending sorted arrays
    if arr[Pivot] == target:
        return Pivot
    start = 0
    if arr[start] <= target:
        # Search on left side of pivot
        return BinarySearch(arr, 0, Pivot - 1, target)
    else:
        # Search on right side of pivot
        return BinarySearch(arr, Pivot + 1, len(arr) - 1, target)

# arr = [4, 5, 6, 7, 0, 1, 2]
arr = [2,11,11,2,2]
target = 2

ans = RoatedBS(arr, target)
# print(ans)
