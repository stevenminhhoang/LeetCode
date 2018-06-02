# 2 dictionaries
def isomorphic_strings(s, t):
    dic_s = {}
    dic_t = {}
    for i in range(len(s)):
        dic_s[s[i]] = t[i]
        dic_t[t[i]] = s[i]


    for i in range(len(t)):
        if t[i] != dic_s[s[i]] or s[i] != dic_t[t[i]]:
            return False

    return True

print(isomorphic_strings("aa", "ab"))
