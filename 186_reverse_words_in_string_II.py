def reverseWords(str):
    def reverse(s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    reverse(str, 0, len(str) - 1)
    start = 0
    for i in range(len(str)):
        if str[i] == " ":
            reverse(str, start, i - 1)
            start = i + 1

    reverse(str, start, len(str) - 1)
    return str


print(reverseWords(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]))
