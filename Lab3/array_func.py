def set_2d_array(arr, size, isAdd):
    for i in range(size):
        subarr = []
        for j in range(size):
            if isAdd==0:
                subarr.append(int(input()))
            else:
                if(i == j):
                    subarr.append("0")
                else:
                    subarr.append(str(i+1))
        arr.append(subarr)

def print_2d_array(arr):
    for subarr in arr:
        for el in subarr:
            print(str(el).ljust(7) + "| ", end = "")
        print()
        

def find_max(arr):
    maxi = -2**63
    for subarr in arr:
        for el in subarr:
            if el > maxi:
                maxi = el
    return maxi

def reduct_inf(arr, size):
    maxi = find_max(arr) * size
    for i in range(size):
        for j in range(size):
            if(arr[i][j] == -1):
                arr[i][j] = maxi

