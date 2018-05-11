def num_jewels_in_stones(J, S):
    ans = 0
    x = set(J)
    for char in S:
        if char in x:
            ans += 1

    return ans

print(num_jewels_in_stones("z", "ZZ"))
