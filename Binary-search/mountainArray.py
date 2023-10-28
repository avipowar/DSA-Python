# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

def MontainArray(arr):

    start = 0
    end = len(arr) - 1

    while(start < end):
        
        mid = (start + end) // 2

        if arr[mid] > arr[mid+1]:
            # this may be the ans but look at the left
            #you are in descending part of the array
            # may be the ans this why end != mid - 1
            end = mid 
           
            
        else:
            # arr[mid] < arr[mid+1]
            # why mid + 1 because i know the my mid+1 is greater tha mid 
            start = mid + 1  #you are in Ascending part of the array
    # in the end start == end pointing to the lagrest number because of the two checks above
    # start and end are always trying to find max element above two checks
    return start # or return end as both are equal

arr = [1, 2, 3, 5, 6, 4, 3, 2]
ans = MontainArray(arr)
print(ans)
