# O(n * 2)
def pathSum(self, root, sum):
    def pathSumFrom(node, sum):
        if not node:
            return 0

        return int(node.val == sum) + pathSumFrom(node.left, sum - node.val) + pathSumFrom(node.right, sum - node.val)

    if not root:
        return 0

    return pathSumFrom(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

# O(N)
def pathSum(self, root, sum):
    def dfs(root, target, curr_path_sum, cache):
        global count
        if not root:
            return

        curr_path_sum += root.val
        old_path_sum = curr_path_sum - target

        count += cache.get(old_path_sum, 0)
        cache[curr_path_sum] = cache.get(curr_path_sum, 0) + 1
        # dfs
        dfs(root.left, target, curr_path_sum, cache)
        dfs(root.right, target, curr_path_sum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[curr_path_sum] -= 1
        return count


    global count
    count = 0
    cache = {0:1}
    dfs(root, sum, 0, cache)
    return count
