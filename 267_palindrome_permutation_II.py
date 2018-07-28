def generate_palindrome(s):
    def backtrack(lis, start, s, odd_char):
        if start == len(s):
            if odd_char == 0:
                lis.add("".join(s[:] + s[::-1]))
            else:
                lis.add("".join(s[:] + odd_char + s[::-1]))
        else:
            for i in range(start, len(s)):
                if s[i] == s[start] and start != i:
                    continue
                s[start], s[i] = s[i], s[start]
                backtrack(lis, start + 1, s, odd_char)
                s[start], s[i] = s[i], s[start]

    def can_permute_palindrome(s, map):
        count = 0
        for char in s:
            map[ord(char)] += 1
            if map[ord(char)] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1

    map = [0 for i in range(128)]
    string = []
    odd_char = 0
    if not can_permute_palindrome(s, map):
        return []

    for i in range(128):
        if map[i] % 2 == 1:
            odd_char = [chr(i)]
        for j in range(map[i] // 2):
            string.append(chr(i))

    lis = set()
    backtrack(lis, 0, string, odd_char)
    return list(lis)

print(generate_palindrome("a"))
print(generate_palindrome("aabbhijkkjih"))
