def repeated_substring_pattern(s):
    if not s:
        return False

    return s in (s+s)[1:-1]

print(repeated_substring_pattern("abcabcabcabc"))
