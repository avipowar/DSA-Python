# order agnostic means two types of array mixture asend array and decending array
# order ognostic Binary Search

def OrderOgnosticBS(arr, target):
    start = 0
    end = len(arr) - 1

    # find the arrays are sorted in acending order decending
    
    isAce = arr[start] < arr[end] 


    while(start <= end):
        # // use these because i want int value
        # calculate mid
        mid = (start + end) // 2

        if (target == arr[mid]):
            return mid

        if isAce:
         #  Asending Order
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1  
        else:
            # Decending Order
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
     # ans doesnot found          
    return -1

# Ascending Order
# arr = [-18, -12, -4, 0, 2, 3, 4, 15, 16, 18, 22, 89, 95]   
# Decending Order
arr = [40, 33, 31, 29, 20, 15, 12, 10, 5, 1, 0]
target = 20

ans = print(OrderOgnosticBS(arr,target))
print(ans)

                    
