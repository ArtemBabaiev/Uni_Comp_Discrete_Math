import re
from class_implicant import *
from functions import *
#1011010110100100
#0.2.3.5.7.8.10.13
#0000+0010+1000+0011+0101+1010+0111+1101
# *0*0+*101+0*11

# 25 - 00011001
# 3
# 4
# 7
if True:
    method = input("1 - Векторний; 2 - Порядковий номер; 3 - Куби\nОберіть метод задання функції: ")
    minterms = []
    num_of_var = None
    isFind = None

    if method == "1":
        vect = input("Введіть вектор: ")
        if check_len(len(vect), 2):
            num_of_var = find_num_vector(len(vect))
            if all_zeros(vect):
                print("f = 0")
                isFind = False
            elif all_ones(vect):
                print("f = 1")
                isFind = False
            else:
                for i in range(len(vect)):
                    if vect[i] == "1":
                        minterms.append(Implicant(dec_to_bin(i, num_of_var), False, [], False))
                isFind = True
        else:
            isFind = False
            print("Вектор введено неправильно")
    
    elif method == "2":
        num = bin(int(input("Введіть номер: ")))[2:]
        num = correctVector(num, 2)
        print("Вектор: {vec}".format(vec = num))
        num_of_var = find_num_vector(len(num))
        if all_zeros(num):
            print("f = 0")
            isFind = False
        elif all_ones(num):
            print("f = 1")
            isFind = False
        else:
            for i in range(len(num)):
                if num[i] == "1":
                    minterms.append(Implicant(dec_to_bin(i, num_of_var), False, [], False))
            isFind = True


    elif method == "3":
        expr = input("Введіть ДДНФ (диз = +): ")
        arr = expr.split("+")
        num_of_var = len(arr[0])
        tempOK = True
        for i in range(len(arr)):
            if num_of_var != len(arr[i]):
                print("куби містять різну кількість цифр:")
                tempOK = False
                break
            if len(re.findall(r"[^01]", arr[i])):
                print("Містить неможливі символи")
                tempOK = False
                break
        if tempOK:
            for i in range(len(arr)):
                minterms.append(Implicant(arr[i], False, [], False))
            isFind = True
        else:
            isFind = False
    
    
    if isFind:
        print("Конституенти 1: ",end="")
        for el in minterms:
            print(el.Name, end=" | ")
        print()
        #print("Коституенти 1: %s" % minterms)
        print("Кількість змінних: %s" % num_of_var)
        groups = {a: [] for a in range(0, num_of_var+1)}
        for el in minterms:
            num_one = 0
            for i in range(len(el.Name)):
                if el.Name[i] == "1":
                    num_one+=1
            groups[num_one].append(el)
        #print(groups)
        rpl_group = {a: [] for a in range(1, num_of_var+1)}
        for i in range(num_of_var):
            if len(groups[i]) == 0 or len(groups[i+1]) == 0:
                continue
            for j in range(len(groups[i])):
                for k in range(len(groups[i+1])):
                    if num_of_diff(groups[i][j].Name, groups[i+1][k].Name) == 1:
                        groups[i][j].IsUsed = True
                        groups[i+1][k].IsUsed = True
                        elem = pasting(groups[i][j].Name, groups[i+1][k].Name)
                        rpl_group[elem.index("*") + 1].append(Implicant(elem, False, [], False))               

        arr = []
        for i in range(1, num_of_var+1):
            if len(rpl_group[i]) == 0:
                continue
            for j in range(len(rpl_group[i])):
                for k in range(j, len(rpl_group[i])):
                    if num_of_diff(rpl_group[i][j].Name, rpl_group[i][k].Name) == 1:
                        rpl_group[i][j].IsUsed = True
                        rpl_group[i][k].IsUsed = True
                        pasted = pasting(rpl_group[i][j].Name, rpl_group[i][k].Name)
                        if not pasted in arr:
                            arr.append(pasted)        

        for i in range(len(arr)):
            temp = arr.pop(i)
            arr.insert(i, Implicant(temp, False, [], True))
        for i in range(1, num_of_var+1):
            for j in range(len(rpl_group[i])):
                if rpl_group[i][j].IsUsed == False:
                    rpl_group[i][j].IsUsed = True
                    arr.append(rpl_group[i][j])
        for i in range(0, num_of_var+1):
            for j in range(len(groups[i])):
                if groups[i][j].IsUsed == False:
                    groups[i][j].IsUsed = True
                    arr.append(groups[i][j])

        table = [["-" for i in range(len(minterms) + 1)] for i in range(len(arr)+1)]
        colums = len(table[0])
        rows = len(table)
        k = 0
        l = 0
        for i in range(rows):
            for j in range(colums):
                if i==0 and j != 0:
                    table[i][j] = minterms[k]
                    k += 1
                elif j==0 and i!=0:
                    table[i][j] = arr[l]
                    l+=1
        for i in range(1, rows):        #Чи покриває
            for j in range(1, colums):
                if is_cover(table[i][0].Name, table[0][j].Name):
                    table[i][j] = "+"
                    table[i][0].ToCover = table[0][j]
        for j in range(1, colums):
            counter = 0
            index = None
            for i in range(1, rows):
                if table[i][j] == "+":
                    counter+=1
                    index = i
            if counter == 1:
                table[index][0].IsCore = True
        Cores = []
        copytable = []
        for i in range(len(table)):
            copytable.append(table[i].copy())    
        for i in range(1, rows):
            if table[i][0].IsCore == True:
                Cores.append(table[i][0].Name)
                for j in range(1, colums):
                    if table[i][j] == "+":
                        copytable[i][j] = "$"
                        table[i][j] = "$"
                        table[0][j] = True
        #print(Cores)
        printTable(copytable)
        print(125*'*')
        #printTable(table)
        variants = []
        for j in range(1, colums):
            if table[0][j] != True:
                subarr = []
                for i in range(1, rows):
                    if table[i][j] == "+":
                        subarr.append(table[i][0].Name)
                variants.append(subarr)
        variants = allCombinations(variants)
        deadends = []
        for V in variants:
            tym = "+".join(Cores + V)
            tym = re.sub(r"(\+\+)", "+", tym)
            if tym[0] == "+":
                tym = tym.replace("+", "", 1)
            if tym[len(tym)-1] == "+":
                tymarr = re.split(r"", tym)
                tymarr[len(tymarr)-2] = ""
                tym = "".join(tymarr)
            deadends.append(tym)
        print("Тупикові форми: ", end="")
        print(deadends)
        minel = 2**60
        minimal = None
        for i in range(len(deadends)):
            if len(re.split(r"\+", deadends[i])) < minel:
                minel = len(re.split(r"\+", deadends[i]))
                minimal = deadends[i]
        print("МДНФ: %s" % minimal)
        # for el in arr:
        #     el.printInfo()


    