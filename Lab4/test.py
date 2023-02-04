        # star_group = {a: [[],[]] for a in range(1, num_of_var+1)}

        # for i in range(num_of_var):
        #     if len(groups[i]) == 0 or len(groups[i+1])==0:
        #         continue
        #     for j in range(len(groups[i])):
        #         for k in range(len(groups[i+1])):
        #             if num_of_diff(groups[i][j], groups[i+1][k]) == 1:
        #                 elem = pasting(groups[i][j], groups[i+1][k])
        #                 star_group[elem.index("*") + 1][0].append(elem)
        #                 star_group[elem.index("*") + 1][1].append(False)
        # print(star_group)
        # arr = []
        # for i in range(1, num_of_var+1):
        #     if len(star_group[i]) ==0:
        #         continue
        #     for j in range(len(star_group[i][0])):
        #         star_group[i][0][j]
        #         for k in range(j, len(star_group[i][0])):
        #             if num_of_diff(star_group[i][0][j], star_group[i][0][k]) == 1:
        #                 star_group[i][1][j] = True
        #                 star_group[i][1][k] = True
        #                 pasted = pasting(star_group[i][0][j], star_group[i][0][k])
        #                 if not pasted in arr:
        #                     arr.append(pasted)
        
        # for i in range(1, num_of_var+1):
        #     for j in range(len(star_group[i][1])):
        #         if star_group[i][1][j] == False:
        #             arr.append(star_group[i][0][j])
        # print("*"*150)
        # print(arr)
        # table = [["-" for i in range(len(minterms) + 1)] for i in range(len(arr)+1)]
        # k = 0
        # l = 0
        # colums = len(table[0])
        # rows = len(table)
        # for i in range(rows):
        #     for j in range(colums):
        #         if i==0 and j==0:
        #             table[i][j] = "@"
        #         elif i==0 and j!=0:
        #             table[i][j] = minterms[k]
        #             k+=1
        #         elif j==0 and i!=0:
        #             table[i][j] = arr[l]
        #             l+=1
        # for i in range(1, rows):
        #     for j in range(1, colums):
        #         if is_cover(table[i][0], table[0][j]):
        #             table[i][j] = "+"

        # for sub in table:
        #     for el in sub:
        #         print(str(el).ljust(5), end = "| ")
        #     print()
        
        # Cores = [False for i in range(len(arr))]
        # stringCores = ""
        # for j in range(1, colums):
        #     counter = 0
        #     index = -1
        #     for i in range(1, rows):
        #         if table[i][j] == "+":
        #             counter+=1
        #             index = i-1
        #     if counter == 1:
        #         Cores[index] = True
        
        # print("*"*160)
        # for sub in table:
        #     for el in sub:
        #         print(str(el).ljust(5), end = "| ")
        #     print()
        

        # for i in range(1, rows):
        #     if Cores[i-1] == True:
        #         stringCores+= "%s+" % table[i][0]
        #         for j in range(1, colums):
        #             if table[i][j] == "+":
        #                 table[i][j] = "$"
        #                 table[0][j] = True
        # print(Cores)
        # print(stringCores)




        
        # print("*"*160)
        # for sub in table:
        #     for el in sub:
        #         print(str(el).ljust(5), end = "| ")
        #     print()
        # print(stringCores)