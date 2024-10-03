numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    if i == 1 or i == 0:
        continue
    is_prime = 1
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if not is_prime:
        not_primes.append(i)
        continue
    primes.append(i)

print(f'primes: {primes}')
print(f'not_primes: {not_primes}')
