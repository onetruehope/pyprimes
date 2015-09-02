"""
file:primes.py
author:Andrew Berson
"""
def gen_primes():
    n = 2
    primes = set()
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.add(n)
            yield n
        n += 1
x = int(input("Find primes under what value?\n"))
primes = gen_primes()
for i in primes:
    if i < x:
        print(i,end=' ')
    else:
        break
