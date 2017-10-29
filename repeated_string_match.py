def repeated_string_match(A, B):
    times = -(-len(B) // len(A)) # ceil(len(B)/len(A))
    # print(A * times)
    # print(A * (times + 1))
    if B in (A * times):
        return times
    elif B in (A * (times + 1)):
        return times + 1
    else:
        return -1

print(repeated_string_match("abcd","cdabcdab"))
