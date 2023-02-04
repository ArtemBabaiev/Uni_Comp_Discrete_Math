from array_func import *
           
def find_path(arr, start, indX, indY):
    if arr[indX][indY] == str(start):
        return ""
    else:
        return arr[indX][indY][-1] + "->" + find_path(arr, start, indX, int(arr[indX][indY][-1]) - 1)



if True:
    print()
    #matrix = [[0,-3,-5, 1000], [1000,0,-3,8], [1000,1000,0,1000], [1000,1000,4, 0]]
    #matrix = [[0, 4, 6, -1, -1, 3], [-1, 0, 7, 1, 2, -1], [-1, -1, 0, 8,-1, -1], [-1, -1, -1, 0, 2, 8], [-1, -1, -1, -1, 0, -1], [-1, -1, -1, -1, -1, 0]]
    #matrix = [[0, -1, 9, -1, 2, 9], [-1, 0, 8,-1, -1, -1], [9, 8, 0,-1,-1,-1], [-1, -1,-1,0,-1,5], [2, -1,-1,-1, 0, 9], [9,-1,-1, 5, 9, 0]]
    matrix = [[0, 4, -1, 3, -1, -1], [-1, 0, 3 , -1, -1, -1], [-1, -1 , 0, 2, -1, 4], [-1, -1, -1, 0, 5, -1], [-1, 1, -1, -1, 0, 3], [-1, -1, -1, -1, -1, 0]]
    add_matrix = []
    num_of_elemnts = 6
    #num_of_elemnts = int(input("Введіть кількість елементів"))
    #set_2d_array(matrix,num_of_elemnts, 0)
    #print_2d_array(matrix, num_of_elemnts)
    reduct_inf(matrix, num_of_elemnts)
    set_2d_array(add_matrix, num_of_elemnts, 1)
    print("Матриця ваг:")
    print_2d_array(matrix)
    # print("Допоміжна матриця:")
    # print_2d_array(add_matrix)
    for k in range(num_of_elemnts):
        for i in range(num_of_elemnts):
            if i == k:
                continue
            for j in range(num_of_elemnts):
                if j==k:
                    continue
                sum =  matrix[i][k] + matrix[k][j]
                if sum < matrix[i][j]:
                    matrix[i][j] = sum
                    add_matrix[i][j] = str(add_matrix[i][j]) + "->" + str(k+1) 
    print("Результуча матриця:")
    print_2d_array(matrix)
    print("Допоміжна матриця:")
    print_2d_array(add_matrix)
    maxi = find_max(matrix)
    for i in range(num_of_elemnts):
        for j in range(num_of_elemnts):
            if matrix[i][j] == 0:
                print("Шлях з %s у %s: 0" % (i+1, j+1))
            elif matrix[i][j] == maxi:
                print("Шлях з %s у %s не існує" % (i+1, j+1))
            else:
                print("Шлях з %s у %s:" % (i+1, j+1), end=" ")
                if len(add_matrix[i][j]) == 1:
                    print(add_matrix[i][j] + "->" + str(j+1))
                else:
                        print(add_matrix[i][j][0] + "->" + find_path(add_matrix, int(add_matrix[i][j][0]), i, int(add_matrix[i][j][-1]) - 1) + add_matrix[i][j][-1:] + "->" + str(j+1))
input()	