# https://leetcode.com/problems/richest-customer-wealth/


def MaxmumWealth(arr):

    # Store the account answer

    ans = 0

    # length of arr

    sizeofArray = len(arr)

    # Person is Row

    # Account is col

    for person in range(0, sizeofArray):

     # When you start the new col  , can take a new sum for that row

        sum = 0

        for account in range(0, len(arr[person])):

            sum += arr[person][account]

         # Now we have some of acccount of person

         # check with overall ans

        if (sum > ans):

            ans = sum

    return sum


arr = [


    [1, 2, 3],


    [2, 4, 6],


    [12, 2, 1]


]

# call the function


print(MaxmumWealth(arr))
