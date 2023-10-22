# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/


# shortcut find the numbers of digit
def DigitCount(num):


    # number is negative
    if (num < 0):
        num = num * -1

    # number is 1
    if(num == 0):
        return 1 

    # count the numbers
    counter = 0

    while(num > 0):

        counter = counter + 1
        # it skip last number and gives the remaining number
        num = num // 10

    return counter



def even(num):

    # call the function and check how many digits in a number
    numDigits = DigitCount(num)


    if(numDigits % 2 == 0):

        return True
    else:

        return False


     # you can write shortcut

     # numDigits % 2 == 0 


def FindNumbers(arr):

    # size of array

    sizeofArray = len(arr)


    # count the numbers

    count = 0

    # run a loop

    for i in range(sizeofArray):
    #   call the even function check number is even or not
        if(even(arr[i])):

            count = count + 1

    return count


# declear the array  

arr = [12,245,2,6,7896]

# call the function

# print(FindNumbers(arr))
print(DigitCount(-1234512212))
# print(DigitCount2(-1234512212))