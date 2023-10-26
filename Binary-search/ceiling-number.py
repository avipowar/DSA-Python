# return thr iddex
# if the element does not exist return -1
# smallest number greater than equal to target
def CeilingOfTheGivenN(arr , target):
# but what if target element is greather tahn the greatest element in the array 
    if(target > arr[len(arr) - 1]):
        return -1

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
        elif (target == arr[mid]):
            return arr[mid]

         # number not foud the entire loop return the start index because at the end. start = mid +1 it gives a maximum of minmum number 
    return arr[start]      

   

arr = [-18, -12, -4, 0, 2, 3, 4, 15, 16, 18, 22, 89, 95]   
target = 177

print(CeilingOfTheGivenN(arr,target))




