def swap_two_letters(A, B):
    if len(A) != len(B):
        return False

    count = 0
    i = 0
    prev = curr = -1
    while i < len(A):
        if A[i] != B[i]:
            count += 1
            if count > 2:
                return False

            prev = curr
            curr = i

        i += 1

    return count == 2 and A[prev] == B[curr] and A[curr] == B[prev]

print(swap_two_letters("geeks", "keegs"))
