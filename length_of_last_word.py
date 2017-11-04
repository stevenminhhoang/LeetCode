def length_of_last_word(s):
    if not s:
        return 0
    if s[-1] == ' ':
        return 0
    else:
        return len(s.strip('').split('')[-1])

print(length_of_last_word("a "))
