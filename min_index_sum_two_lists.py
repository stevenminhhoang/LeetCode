# O(m * n)
# def find_restaurant(list1, list2):
#     dic = {}
#     for i, x in enumerate(list1):
#         for j, y in enumerate(list2):
#             if x == y:
#                 dic[x] = i + j
#     min_val = min(dic.values())
#
#     return [r for r in dic if dic[r] == min_val]
#


# O(m + n)
def find_restaurant_2(list1, list2):
    dict1 = {rest: i for i, rest in enumerate(list1)}
    dict2 = {rest: i for i, rest in enumerate(list2)}
    dict_sum = {rest: dict1[rest] + dict2[rest] for rest in list1 if rest in list2}
    min_val = min(dict_sum.values())

    return [r for r in dict_sum if dict_sum[r] == min_val]

print(find_restaurant_2(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Tapioca Express", "Shogun", "KFC", "Burger King"]))
