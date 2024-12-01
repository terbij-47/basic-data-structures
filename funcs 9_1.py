def apply_all_func(int_list : list[int | float], *funcs) -> dict[str, int | float | list]:
    res_dict = {}
    for func in funcs:
        res_dict[func.__name__] = func(int_list)
    return res_dict

print(apply_all_func([1, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
