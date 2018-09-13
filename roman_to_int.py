def roman_to_int(s):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    ans = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            ans = ans - roman[s[i]]
        else:
            ans = ans + roman[s[i]]

    return ans + roman[s[-1]]

print(roman_to_int("MCMXCIV"))
