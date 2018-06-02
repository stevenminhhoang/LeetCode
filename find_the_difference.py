def find_the_difference(s, t):
    return chr((sum(ord(c) for c in t) - sum(ord(c) for c in s)))

find_the_difference("abcd", "bcdas")
