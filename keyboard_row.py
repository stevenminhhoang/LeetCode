def keyboard_row(words):
    ans = []
    first_row = set('qwertyuiop')
    second_row = set('asdfghjkl')
    third_row = set('zxcvbnm')
    for word in words:
        data = set(word.lower())
        if data&first_row == data or data&second_row == data or data&third_row == data:
            ans.append(word)

    return ans

print(keyboard_row(["Hello", "Alaska", "Dad", "Peace"]))
