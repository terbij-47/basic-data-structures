def all_variants(text : str):
    for count in range(1, len(text) + 1):
        for start in range(len(text) + 1 - count):
            yield text[start : start + count]

a = all_variants("abcde")
for i in a:
    print(i)
