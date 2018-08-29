import collections
def word_ladder_II(start, end, word_list):
    word_dict = set(word_list)
    res = []
    neighbor = collections.defaultdict(list)
    distance = 
