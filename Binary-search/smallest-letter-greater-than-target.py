# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

def nxtGreaterLetter(char, target):

    start = 0
    end = len(char)-1

    while start <= end:
        
        mid = (start+end) // 2

        if target < char[mid]:
            end = mid - 1
        else:
            start = mid + 1

#   you can write also
    return char[start % len(char)]  

    # you can write also 
    # if (start == len(char)):
    #     return char[0]
    # else:
    #     return char[start]         


char = ['a', 'b', 'c', 'd']
target = 'c'
print(nxtGreaterLetter(char, target))

