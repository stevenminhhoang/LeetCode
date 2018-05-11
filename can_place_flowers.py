def can_place_flowers(flowerbed, n):
    i = 0
    count = 0
    while i < len(flowerbed):
        if (flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
            flowerbed[i] = 1
            count += 1

        i += 1

    return count >= n

print(can_place_flowers([0, 0, 0, 0, 0], 4))
