my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(my_list) and my_list[i] >= 0:
    i += 1
    if my_list[i - 1] == 0:
        continue
    print(my_list[i - 1])    
