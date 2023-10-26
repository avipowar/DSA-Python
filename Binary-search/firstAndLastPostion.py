# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# this function also return the index value of target
def search(arr, target, FirsIndex):
    start = 0
    end = len(arr) - 1
    ans = -1
    while start <= end :

        mid = (start+end) // 2
        if arr[mid] > target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            # Potential ans is found
            ans = mid
            # check first and last occurence here
            if(FirsIndex):
                end = mid - 1
            else:
                start = mid + 1

    return ans            


def FirstAndLastPostion(arr, target):

    ans = [-1, -1]
    # First Occurence
    FirstIndex = True
    firstPostion = search(arr, target, FirstIndex)
    # if ans[0] != -1:
    #     lastPostion = search(arr, target, FirstIndex)
    # Last Occurence
    FirstIndex = False
    lastPostion = search(arr, target, FirstIndex)
    # Finasl ans return
    ans[0] = firstPostion
    ans[1] = lastPostion

    return ans


arr = [5, 7, 7, 7, 7, 8, 8, 10]
target = 7

# function calling
ans = FirstAndLastPostion(arr, target)
print(ans)