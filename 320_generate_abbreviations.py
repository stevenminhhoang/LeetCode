# O(n * 2^n)
def generate_abbreviations(word):
    def backtrack(lis, temp, start, count, word):
        if start == len(word):
            if count > 0:
                temp += str(count)
            lis.append(temp)
        else:
            # Keep current position
            backtrack(lis, temp + (str(count) if count > 0 else '') + word[start], start + 1, 0, word)
            # Skip, abbreviate current position
            backtrack(lis, temp, start + 1, count + 1, word)

    lis = []
    backtrack(lis, "", 0, 0, word)
    return lis

print(generate_abbreviations("word"))
