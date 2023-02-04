from array_func import *

def set_matrix(arr, size):
    for i in range(size):
        subarr = []
        for j in range(size):
            subarr.append(int(input()))
        arr.append(subarr)

#                       1        3
def find_path(table, proobraz, obraz):
    index = obraz - 1
    if table[1][index] == 1:
        return str(obraz)
    elif(table[1][index] == proobraz):
        return str(proobraz) + "->" +str(obraz)
    else:
        return str(proobraz) + "->" + find_path(table, table[1][table[1][index]-1] ,table[1][index])

if True:
    print()
    #matrix = [[0,0,0,0,1,1,0], [1,0,1,0,1,0,1], [1,1,0,1,1,0,0], [0,0,1,0,1,1,0], [1,0,0,1,0,1,0], [0,0,1,0,1,0,0], [1,1,0,1,1,0,0]]
    #num_of_elemnts = 7
    num_of_elemnts = 4
    matrix = [[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]]
    #num_of_elemnts = int(input("Введіть кількість елементів: "))
    #set_matrix(matrix, num_of_elemnts)
    print("Матриця суміжності")
    print_2d_array(matrix)
    waves = {0: {1}}
    proobraz = [[(k+1) for k in range(num_of_elemnts) ], [-1 for k in range(num_of_elemnts)]]
    proobraz[1][0] = "-"
    print_2d_array(proobraz)
    FW = {1}
    i = 0
    while True:
        FWi = set()
        D = set()
        for el in waves[i]:
            for j in range(num_of_elemnts):
                if matrix[el-1][j] == 1:
                    D.add(j+1)
                    if (proobraz[1][j] == -1):
                        proobraz[1][j] = el
        FWi = D.difference(FW)
        if len(FWi) == 0:
            break
        FW = FW.union(FWi)
        i+=1
        waves[i] = FWi
        #print(waves)
    print("\nХвилі")
    print(waves)      
    print("\nТабличка прообразів")
    print_2d_array(proobraz)

    print("*"*100)
    for j in range(num_of_elemnts):
        if proobraz[1][j] == -1:
            print("Шляху з 1 y %s не існує" %(j+1))
        elif proobraz[1][j] == "-":
            print("Шляху з 1-ої вершини y %s дорівнює 0" %(j+1))
        else:
            print("Шлях з 1 у %s" % (j+1), end = ": ")
            if(proobraz[1][j] == 1):
                print(str(proobraz[1][j]) + "->" + str(proobraz[0][j]))
            else:
                print(find_path(proobraz, 1, proobraz[0][j]) + "->" + str(j+1))
             

                 