# O(n)
def length_of_longest_substring(s):
    if not s:
        return 0

    visited = {}
    start, end = 0, 0
    length = 0
    ans = ""

    while end < len(s):
        end_char = s[end]
        if end_char in visited and start <= visited[end_char]:
            start = visited[end_char] + 1

        visited[end_char] = end
        end += 1

        if end - start > length:
            length = end - start
            ans = s[start:end]

    return length


print(length_of_longest_substring("abcabcbb"))
