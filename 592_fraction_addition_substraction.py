import re
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)

def fraction_addition(expression):
    ls = re.split(r"[+-]", expression)
    sign = []
    if expression[0] != '-':
        sign.append('+')

    for char in expression:
        if char == '+' or char == '-':
            sign.append(char)

    prev_numerator, prev_denominator = 0, 1
    i = 0
    for num in ls:
        if len(num) > 0:
            numerator, denominator = map(int, num.split("/"))
            g = abs(gcd(prev_denominator, denominator))
            lcm = prev_denominator * denominator // g
            if sign[i] == '+':
                prev_numerator = prev_numerator * lcm // prev_denominator + numerator * lcm // denominator
            else:
                prev_numerator = prev_numerator * lcm // prev_denominator - numerator * lcm // denominator

            prev_denominator = lcm
            g = abs(gcd(prev_numerator, prev_denominator))
            prev_numerator //= g
            prev_denominator //= g
            i += 1

    return "{}/{}".format(prev_numerator, prev_denominator)






print(fraction_addition("1/2+1/3"))
print(fraction_addition("-1/2+1/2"))
print(fraction_addition("1/3-1/2"))
print(fraction_addition("5/3+1/3"))
