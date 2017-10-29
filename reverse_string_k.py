def reverse_string_II(s, k):
    n = len(s)
    s = list(s)
    mod = n%(2*k)
    if n <= k:
        return ''.join(s[::-1])

    for i in range(0,n-mod,2*k):
        s[i:i+k] = s[i:i+k][::-1]

    if mod < k and mod > 0:
        s[n-mod:] = s[n-mod:][::-1]
        
    if mod >= k and mod < 2 * k:
        s[n-mod:n-mod+k] = s[n-mod:n-mod+k][::-1]

    return ''.join(s)

# print(reverse_string_II("abcdefg", 4))
# print(reverse_string_II("abcdefghijk", 4))
# print(reverse_string_II("abcdefgh",2))
print(reverse_string_II("abcdefg", 2))
# print(reverse_string_II("abcd", 4))
# print(reverse_string_II("krmyfshbspcgtesxnnljhfursyissjnsocgdhgfxubewllxzqhpasguvlrxtkgatzfybprfmmfithphckksnvjkcvnsqgsgosfxc",
# 20))
