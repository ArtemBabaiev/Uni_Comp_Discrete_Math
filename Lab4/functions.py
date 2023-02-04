from class_implicant import *

def dec_to_bin(x, num):
    string = bin(x)[2:]
    while True:
        if len(string) == num:
            return string
        else:
            string = "0" + string
    
def all_zeros(arr):
    zeros = True
    for el in arr:
        if el=="1":
            return False
    return zeros

def all_ones(arr):
    ones = True
    for el in arr:
        if el=="0":
            return False
    return ones

def check_len(length, match):
    if length == match:
        return True
    elif length < 2 or match > length:
        return False
    else:
        return check_len(length, 2*match)

def find_num_vector(length):
    for i in range(length):
        if 2**i == length:
            return i

def find_num_num(maxi):
    i = 1
    while True:
        match = 2**i
        if maxi <= match:
            return i
        elif maxi>match:
            i+=1

def num_of_diff(first, second):
    num_of_diffs=0
    for i in range(len(first)):
        if first[i] != second[i]:
            num_of_diffs +=1
    return num_of_diffs

def pasting(first, second):
    string = list(first)
    for i in range(len(first)):
        if first[i] != second[i]:
            string[i] = "*"
    return "".join(string)

def is_cover(imp, toCover):
    isCover = True
    for i in range(len(imp)):
        if imp[i] == "*":
            continue
        else:
            if imp[i]!=toCover[i]:
                isCover = False
    return isCover

def printTable(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if j==0 and i!=0:
                print(str(table[i][j].Name).ljust(6), end = "| ")
            elif i == 0 and j!=0:
                if isinstance(table[i][j], Implicant):
                    print(str(table[i][j].Name).ljust(6), end = "| ")
                else:
                    print(str(table[i][j]).ljust(6), end = "| ")
            else:
                print(str(table[i][j]).ljust(6), end = "| ")
        print()

def del_repit(arr):
    for subarr in arr:
        for i in range(len(subarr)):
            temp = subarr.pop(i)
            if not temp in subarr:
                subarr.insert(i, temp)
            else:
                subarr.insert(i, "")
    return arr

def allCombinations(arr):
    n = len(arr)
    indices = [0 for i in range(n)]
    allComb = []
    while (1):
        string = []
        for i in range(n):
            string.append(arr[i][indices[i]])
        allComb.append(string)
        next = n - 1
        while (next >= 0 and
              (indices[next] + 1 >= len(arr[next]))):
            next-=1
 
        if (next < 0):
            allComb = del_repit(allComb)
            return allComb
 
        indices[next] += 1
 
        for i in range(next + 1, n):
            indices[i] = 0

def correctVector(n, match):
    if len(n) < match:
        n = (match - len(n))*"0" + n
        return n
    elif len(n) == match:
        return n
    else:
        return correctVector(n, 2*match)



