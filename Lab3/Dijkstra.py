from array_func import *

def set_table(arr, row, column, inf):
    for i in range(row):
        subarr = []
        for j in range(column):
            if i == 0:
                subarr.append(j+1)
            elif i == 1:
                if j == 0:
                    subarr.append(0)
                else:
                    subarr.append(inf)
            elif i == 2:
                if j == 0:
                    subarr.append("-")
                else:
                    subarr.append(0)
            else:
                if j == 0:
                    subarr.append(False)
                else:
                    subarr.append(False)
        arr.append(subarr)           

def alg(matrix,table, maxVal):
    minS = 2**60
    indMin = None   
    for j in range(len(table[1])):
        if table[1][j] < minS and table[3][j] == False:
            minS = table[1][j]
            indMin = j
    for j in range(len(matrix)):
        if matrix[indMin][j] == 0:
            continue
        elif matrix[indMin][j] == maxVal:
            continue
        else:
            if  minS + matrix[indMin][j] < table[1][j] and table[3][j] == False:
                table[1][j] = minS + matrix[indMin][j]
                table[2][j] = indMin+1
    table[3][indMin] = True

def find_path(table, proobraz, obraz):
    index = obraz-1
    if table[2][index] == 1:
        return str(obraz)
    elif(table[2][index] == proobraz):
        return str(proobraz) + "->" +str(obraz)
    else:
        return str(proobraz) + "->" +find_path(table, table[2][table[2][index]-1] ,table[2][index])





if True:
    num_of_elemnts = 4
    matrix = [[0, 2, -1, -1], [-1, 0, 3, -1], [-1, -1, 0, 1], [-1, -1, -1, 0]]
    #num_of_elemnts = int(input("Введіть кількість елементів"))
    #set_2d_array(matrix, num_of_elemnts, 0)
    #matrix = [[0, 4, 6, -1, -1, 3], [-1, 0, 7, 1, 2, -1], [-1, -1, 0, 8,-1, -1], [-1, -1, -1, 0, 2, 8], [-1, -1, -1, -1, 0, -1], [-1, -1, -1, -1, -1, 0]]
    #matrix = [[0, -1, 9, -1, 2, 9], [-1, 0, 8,-1, -1, -1], [9, 8, 0,-1,-1,-1], [-1, -1,-1,0,-1,5], [2, -1,-1,-1, 0, 9], [9,-1,-1, 5, 9, 0]]
    #matrix = [[0, 4, -1, 3, -1, -1], [-1, 0, 3 , -1, -1, -1], [-1, -1 , 0, 2, -1, 4], [-1, -1, -1, 0, 5, -1], [-1, 1, -1, -1, 0, 3], [-1, -1, -1, -1, -1, 0]]
    table = []
    maxi = find_max(matrix) * num_of_elemnts
    reduct_inf(matrix, num_of_elemnts)
    set_table(table, 4, num_of_elemnts, maxi)
    print("Матриця ваг:")
    print_2d_array(matrix)
    print("Табличка")
    print_2d_array(table)
    #alg(matrix, table, maxi)

    #print_2d_array(table)
    array_to_stop = [True for k in range(len(table[3]))]
    while(table[3] != array_to_stop):
        alg(matrix, table, maxi)
    print("Результуча таблиця:")
    print_2d_array(table)
    
    for j in range(len(table[0])):
        if table[1][j] == maxi:
            print("Шляху з 1 y %s не існує" %(j+1))
        elif table[1][j] == 0:
            print("Шляху з 1 y %s: 0" %(j+1))
        else:
            print("Шлях з 1 у %s" % (j+1), end = ": ")
            if(table[2][j] == 1):
                print(str(table[2][j]) + "->" + str(table[0][j]))
            else:
                print(find_path(table, 1, table[0][j]) + "->" + str(j+1))
        print("Довжина шляху %s" % table[1][j])




    
    
    
    

    