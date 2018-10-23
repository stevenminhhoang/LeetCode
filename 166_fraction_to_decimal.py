def fraction_to_decimal(numerator, denominator):
    ans = ""
    dic = {}
    if numerator == 0:
        return "0"
    if (numerator < 0) ^ (denominator < 0):
        ans += "-"

    numerator, denominator = abs(numerator), abs(denominator)
    ans += str(numerator // denominator)
    remainder = numerator % denominator
    if remainder == 0:
        return ans

    ans += "."
    i = len(ans)
    while remainder != 0:
        if remainder not in dic:
            dic[remainder] = i
        else:
            i = dic[remainder]
            ans = ans[:i] + "(" + ans[i:] + ")"
            return ans

        remainder *= 10
        ans += str(remainder // denominator)
        remainder = remainder % denominator
        i += 1

    return ans



print(fraction_to_decimal(3227, 555))
