def swap(arr,s,e):
    temp = arr[s]
    arr[s] = arr[e]
    arr[e] = temp

def reversearray(arr):
    start = 0
    end = len(arr)-1

    while start <= end:
        swap(arr,start, end)
        start = start + 1
        end -= 1
    return arr

arr = [1,2,3,4,5]
print(arr)
result = reversearray(arr)
print(result)