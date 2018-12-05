def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {x: i for i, x in enumerate(B)}
        return [dic[x] for x in A]
