def word_pattern(pattern, str):
    str_arr = str.split(' ')
    if len(pattern) != len(str_arr):
        return False
    dic = {}
    for i in range(len(pattern)):
        if pattern[i] in dic and dic[pattern[i]] != str_arr[i]:
            return False
        else:
            dic[pattern[i]] = str_arr[i]

    return len(set(dic.values())) == len(dic.values())


print(word_pattern("jquery", "jquery"))
print(word_pattern("abba", "dog cat cat dog"))
print(word_pattern("abba", "dog cat cat fish"))
print(word_pattern("aaaa", "dog cat cat dog"))
print(word_pattern("abba", "dog dog dog dog"))
print(word_pattern("abca", "dog cat cat dog"))
