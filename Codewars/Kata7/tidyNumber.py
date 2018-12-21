def tidyNumber(n):
    array=[]
    if len(array) == 1:
        return True
    for num in str(n):
        array.append(num)
    pos=0
    total=0
    while pos < len(array)-1:
        if int(array[pos]) <= int(array[pos+1]):
            total+=1
        else:
            total+=0
        pos+=1
    if total != len(array)-1:
        return False
    else:
        return True



if __name__ == "__main__":

    #Casos Test

    assert tidyNumber(12) == True
    assert tidyNumber(102) == False
    assert tidyNumber(9672) == False
    assert tidyNumber(2789) == True