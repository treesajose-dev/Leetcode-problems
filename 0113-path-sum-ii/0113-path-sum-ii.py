# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, remaining, path):
            if node is None:
                return

            # Add current node to path
            path.append(node.val)
            remaining -= node.val

            # Check if leaf and sum matches
            if node.left is None and node.right is None:
                if remaining == 0:
                    result.append(path[:])

            # Explore children
            dfs(node.left, remaining, path)
            dfs(node.right, remaining, path)

            # Backtrack
            path.pop()

        dfs(root, targetSum, [])

        return result