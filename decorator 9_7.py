def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) != int:
            raise TypeError('Понятие простого/составного числа относится только к целым числам')
        for i in range(2, res):
            if not res % i:
                print('Составное')
                return res
        print('Простое')
        return res
    return wrapper


@is_prime
def sum_three(a : int, b : int, c : int) -> int:
    return a + b + c

print(sum_three(5, 32, 9))
