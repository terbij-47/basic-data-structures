def add_everything_up(a : int | float | str, b : int | float | str) -> int | float | str:
    try:
        result = a + b
    except TypeError:
        result = str(a) + str(b)
    finally:
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
