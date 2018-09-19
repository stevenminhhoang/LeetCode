# O(n)
def decode_string(s):
    if not s:
        return ""

    stack = []
    curr_string = ""
    curr_count = 0
    for char in s:
        if char == "[":
            stack.append(curr_string)
            stack.append(curr_count)
            curr_string = ""
            curr_count = 0
        elif char == "]":
            k = stack.pop()
            prev_string = stack.pop()
            curr_string = prev_string + k * curr_string
        elif char.isdigit():
            curr_count = curr_count * 10 + ord(char) - ord("0")
        else:
            curr_string += char

    return curr_string


print(decode_string("2[a]"))
# print(decode_string("3[a]2[bc]"))
# print(decode_string("3[a2[c]]"))
# print(decode_string("2[abc]3[cd]ef"))
