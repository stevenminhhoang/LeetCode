def even_odd(A):
    A.sort()
    next_even, next_odd = 0, len(A) - 1
    while next_even <= next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1

    return A

print(even_odd([1,6,2,4,3,5,2,4,1,7,8,10,9]))
