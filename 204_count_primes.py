def count_primes(n):
    p = 2
    prime = [True for i in range(n + 1)]
    while p * p <= n:
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1

    return prime[2:n].count(True)

print(count_primes(2))
