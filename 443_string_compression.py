def string_compression(chars):
    anchor = write = 0
    for read, char in enumerate(chars):
        if read == len(chars) - 1 or chars[read + 1] != char:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
                    count = 0

            anchor = read + 1

    return chars[:write]



print(string_compression(["a","a","b","b","c","c","c"]))
print(string_compression(["a"]))
print(string_compression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
