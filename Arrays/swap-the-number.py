def swap(arr,a,b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

arr = [1,2,3,4,5]
# 4 2 3 1 5

print(swap(arr,0,3))   
print(arr)
# [3 2 1 4 5]