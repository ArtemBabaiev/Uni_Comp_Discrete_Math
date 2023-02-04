import os


class Input_Error(Exception):
    pass


def clean_console(): return os.system('cls')


def ReductString(source: str, isSorted: bool) -> str:
    forReduct = list(source)
    forReduct.pop()
    source = "".join(forReduct)
    if not isSorted:
        forReduct = source.split("*")
        intReduct = [int(item) for item in forReduct]
        intReduct.sort()
        forReduct = [str(item) for item in intReduct]
        source = "*".join(forReduct)

    return source


def SimpleDigits(maxi: int) -> list:
    if maxi > 2**16:
        raise Input_Error("Завелике число")
    else:
        arr = []
        for i in range(2, maxi+1):
            isSimple: bool = True
            for j in range(len(arr)):
                if i % arr[j] == 0:
                    isSimple = False
            if isSimple == True:
                arr.append(i)
        return arr


def DecomposeNumber(num: int) -> str:
    if num < 0:
        num = abs(num)
    if num <2:
        return str(num)
    simple = SimpleDigits(num)
    mulipliers = ""
    for simp in simple:
        while True:
            if num % simp == 0:
                num /= simp
                mulipliers += f"{simp}*"
            else:
                break
    mulipliers = ReductString(mulipliers, True)
    return "1*" + mulipliers


def Find_HCK(one: int, two: int):
    if one >= two:
        bigger = DecomposeNumber(one)
        smaller = DecomposeNumber(two)
    else:
        bigger = DecomposeNumber(two)
        smaller = DecomposeNumber(one)
    result = smaller + "*"
    bigger = bigger.split("*")
    for el in bigger:
        if bigger.count(el) > result.count(el):
            result += (el + "*")*(bigger.count(el) - result.count(el))
    result = ReductString(result, False)
    return [result, eval(result)]


def Find_HCD(one: int, two: int):
    result = ""
    if one >= two:
        bigger = DecomposeNumber(one).split("*")
        smaller = DecomposeNumber(two).split("*")
    else:
        bigger = DecomposeNumber(two).split("*")
        smaller = DecomposeNumber(one).split("*")
    for item in smaller:
        if item not in result:
            if item in bigger:
                if smaller.count(item) >= bigger.count(item):
                    result += (item + "*")*bigger.count(item)
                else:
                    result += (item + "*")*smaller.count(item)
    if len(result) == 0:
        return ["-1", -1]
    result = ReductString(result, False)
    return [result, eval(result)]


def Evklid_HCD(one: int, two: int) -> int:
    divider: int
    divided: int
    remainder: int
    fraction: int
    if one > two:
        divider = abs(two)
        divided = abs(one)
    elif two > one:
        divider = abs(one)
        divided = abs(two)
    if divider == 0 or divided == 0:
        return -1
    remainder = divided % divider
    fraction = divided//divider
    while remainder != 0:
        print(f"{divided} = {divider}*{fraction} + {remainder}")
        divided = divider
        divider = remainder
        remainder = divided % divider
        fraction = divided//divider
    if remainder == 0:
        print(f"{divided} = {divider}*{fraction} + {remainder}")
    return divider

def IsMutuallySimple(one: int, two: int) -> bool:
    one = DecomposeNumber(one).split("*")
    two = DecomposeNumber(two)
    for item in one:
        if item in two:
            if item == "1":
                continue
            else:
                return False
    return True

if __name__ == '__main__':
    repit = ""
    while repit != "exit":
        clean_console()
        task = int(input("Введіть номер завдання: "))
        if task == 1:
            print(SimpleDigits(int(input("Введіть максимум: "))))
        elif task == 2:
            print(DecomposeNumber(int(input("Введіть число для розкладу: "))))
        elif task == 3:
            first = int(input("Введіть перше число: "))
            second = int(input("Введіть друге число: "))
            print("НСК: " + str(Find_HCK(first, second)))
            print("НСД: " + str(Find_HCD(first, second)))
            print("*************************************************Евклід*************************************************")
            val = Evklid_HCD(first, second)
            print(f"\nНСД за Евклідом: {val}")
        elif task == 4:
            first = int(input("Введіть перше число: "))
            second = int(input("Введіть друге число: "))
            if IsMutuallySimple(first, second):
                print(f"Числа {first} та {second} взаємно прості")
            else:
                print(f"Числа {first} та {second} НЕ взаємно прості")

        repit = input("\nВведіть exit для завершення: ")
