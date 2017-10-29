def fib(n):
    l = []
    if n == 1 or n == 2:
        l.append(1)
    fib(n-1) + fib(n-2)

print(fib(5))
