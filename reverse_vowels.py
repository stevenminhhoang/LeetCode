def reverse_vowels(s):
    s = list(s)
    vowels = {'a','e','o','u','i','A','E','I','O','U'}
    vowel_in_s = []
    for c in s:
        if c in vowels:
            vowel_in_s.append(c)

    for i in range(len(s)):
        if s[i] in vowels:
            s[i] = vowel_in_s.pop()

    return "".join(s)

print(reverse_vowels("leetcode"))
