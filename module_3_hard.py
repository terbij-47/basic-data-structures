def calculate_structure_sum( data_struct ):
    if isinstance(data_struct, int) or isinstance(data_struct, float):
        return data_struct

    if isinstance(data_struct, str):
        return len(data_struct)

    summ = 0
    if isinstance(data_struct, dict):
        for element in data_struct.items():
            summ += calculate_structure_sum(element)
    else:
        for element in data_struct:
            summ += calculate_structure_sum(element)

    return summ

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
