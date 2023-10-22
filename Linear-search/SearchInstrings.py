def searchInString(string,target):
    # find the size of string
    sizeofString = len(string)

    # run the loop
    for i in range(sizeofString):
        # check the charchter at every index if it is
        if(string[i] == target):
            return i

    # hence the charcter does not found
    return -1
      

string = "AvinashPowar"
target = "r"

print(searchInString(string,target))