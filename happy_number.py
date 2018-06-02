def digit_square_sum(n):
    s = 0
    while n > 0:
        tmp = n % 10
        s += tmp * tmp
        n = n // 10

    return s

def is_happy(n):
    seen = set()
    while n != 1:
        n = digit_square_sum(n)
        if n in seen:
            return False
        else:
            seen.add(n)

    return n == 1
