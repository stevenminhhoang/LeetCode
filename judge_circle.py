def judge_circle(moves):
    x = 0
    y = 0
    for char in moves:
        if char == 'U':
            y += 1
        if char == 'D':
            y -= 1
        if char == 'L':
            x -= 1
        if char == 'R':
            x += 1

    return x == 0 and y == 0

print(judge_circle(''))
print(judge_circle('UUUU'))
print(judge_circle('UDLR'))
print(judge_circle('URDL'))
print(judge_circle('UURDDRLL'))
