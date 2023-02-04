# def met(n, match):
#     if len(n) < match:
#         n = (match - len(n))*"0" + n
#         return n
#     elif len(n) == match:
#         return n
#     else:
#         return met(n, 2*match)



# n = bin(int(input("vv: ")))[2:]
# print(n)
# n = met(n, 2)
# print(n)

a = [[1,2],[3,4]]
b = []
for i in range(len(a)):
    b.append(a[i].copy())
b[0][1] = 7
print(b)
print(a)


# numConst = []
#         print("Введіть номери конституент одиниці:")
#         while True:
#             num = input()
#             if num == "":
#                 break
#             elif len(re.findall(r"[^0-9]", num)) != 0:
#                 print("Введено не допустимий символ")
#             else:
#                 numConst.append(int(num))
#         if len(numConst) != 0:
#             numConst.sort()
#             maxi = max(numConst)
#             num_of_var = find_num_num(maxi)
#             print(num_of_var)

#             if len(bin(num_of_var)[2:]) == len(numConst):
#                 print("Функція має значення 1 на всіх інтерпретаціях\nf = 1")
#                 isFind = False
#             else:
#                 for el in numConst:
#                     minterms.append(Implicant(dec_to_bin(el, num_of_var), False, [], False))
#                 isFind = True
#         else:
#             isFind = False
#             print("Конституент 1 не має\nf = 0")
