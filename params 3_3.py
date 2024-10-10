def print_params(a = 1, b = 'str', c = True):
    print(a, b, c)

print_params()
print_params(4)
print_params(5, 9)
print_params(2, (4, 5), [1, 2, 3])
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [6, 'str', (1, 2, 3)]
values_dict = {'a': True, 'b': 'vb', 'c': [2, 4, 7]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [6, 7]
print_params(*values_list_2, 42)
