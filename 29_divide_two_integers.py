# O(log(n))
def divide(dividend, divisor):
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
    dividend, divisor = abs(dividend), abs(divisor)
    ans = 0

    while dividend >= divisor:
        temp, val = divisor, 1
        while dividend >= temp + temp:
            temp += temp
            val += val

        ans += val
        dividend -= temp


    if sign == -1:
        return max(-2 ** 31, -ans)
    else:
        return min(ans, (2 ** 31) - 1)

print(divide(18, 3))
