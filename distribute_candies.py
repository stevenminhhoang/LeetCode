def distribute_candies(candies):
    candies_set = set(candies)
    return min(len(candies) // 2, len(candies_set))
