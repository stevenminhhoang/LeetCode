import collections, copy
def find_substring(s, words):
    if not s or not words:
        return []

    res = []
    word_size = len(words[0])
    count = collections.Counter(words)
    window_size = word_size * len(words)
    if len(s) < window_size:
        return res

    # we increment begin and end only in word_size
    # there are only word_size possible start points for our window.
    # end is actually the start of the last word in window or put in other words
    # the real end of window is actually at end + word_size
    for i in range(word_size):
        start, end = i, i
        count = copy.copy(count)
        counter = len(count)
        while start + word_size - 1 < len(s):
            last_word = s[end:end + word_size]
            if last_word in count:
                count[last_word] -= 1
                if count[last_word] == 0:
                    counter -= 1

            if end + word_size - start == window_size:
                if counter == 0:
                    res.append(start)

                first_word = s[start:start + word_size]
                if first_word in count:
                    count[first_word] += 1
                    if count[first_word] > 0:
                        counter += 1

                start += word_size

            end += word_size

    return res

print(find_substring("barfoothefoobarman", ["foo","bar"]))
print(find_substring("ababaab", ["ab","ba","ba"]))
