# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        #to check if leaf reached (as leaf no children)
        if root.left== None and root.right== None:
            if targetSum==root.val:
                return True
            else:
                return False

        remaining =targetSum - root.val

        #recursive functions for both child
        LEFTresult = self.hasPathSum(root.left, remaining)
        RIGHTresult = self.hasPathSum(root.right, remaining)

        return LEFTresult or RIGHTresult
        