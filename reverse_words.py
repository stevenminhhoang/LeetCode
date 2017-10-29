def reverse_words(s):
    word_list = [word[::-1] for word in s.split()]
    return " ".join(word_list)

print(reverse_words("Let's take LeetCode contest"))
