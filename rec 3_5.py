# Если я правильно понимаю, алгоритм, предложенный на сайте, не учитывает ситуацию, когда 0 стоит в конце числа.
# Поэтому get_multiplied_digits(1000) выдает 0, хотя мы 0 не учитываем.
# Если проверять нули в рекурсии, то на последних этапах мы не сможем отличить 0 от 1000, да и зачем, если их можно вообще убрать

def get_multiplied_digits_rec( number ):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) <= 1:
        return first
    return first * get_multiplied_digits_rec(int(str_number[1:]))

def get_multiplied_digits( number ):
    if number == 0:
        return 0
    return get_multiplied_digits_rec(int(str(number).replace('0', '')))

print(get_multiplied_digits(40203))
print(get_multiplied_digits(1000))
print(get_multiplied_digits(0))
