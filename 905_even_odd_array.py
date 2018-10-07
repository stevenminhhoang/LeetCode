def sortArrayByParity(A):
        even = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[i], A[even] = A[even], A[i]
                even += 1

        return A

print(sortArrayByParity([3,1,2,4]))
