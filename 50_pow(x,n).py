# O(log(n))
def my_pow(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    if n % 2 == 1:
        return x * my_pow(x, n - 1)

    return my_pow(x * x, n // 2)

print(my_pow(2.000000, 3))
