def hamming_distance(x, y):
    return bin(x ^ y).count('1')

print(hamming_distance(1, 4))
