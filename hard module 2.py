def find_dividers( a ):
    dividers = []
    for i in range(3, a + 1):
        if a % i == 0:
            dividers.append(i)
    return dividers

number = int(input("Введите число: "))
tmp = {}
for el in find_dividers(number):
    for sub in range(1, int((el - 1) / 2) + 1):
        if not tmp.get(sub, False):
           tmp[sub] = [f"{sub}{el - sub}"]
        else:
            tmp.get(sub).append(f"{sub}{el - sub}")
result = ''
for str_arr in list(tmp.values()):
    for st in str_arr:
        result += st
print(f"Пароль: {result}")
