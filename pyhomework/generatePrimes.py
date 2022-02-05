# Generate all of the primes up to limit
# Ishai Masada

prime_list = []
primes = []
limit = int(input('Type in the limit: '))
for num in range(2, (limit+1)):
    prime_list.append(num)
while True:
    if len(prime_list) == 0:
        break
    prime = prime_list[0]
    for elem in prime_list:
        if (elem%prime) == 0:
            primes.append(prime)
            prime_list.remove(elem)
result = [str(prime) for prime in primes]
result = list(set(result))
result.sort()
print(' '.join(result))
