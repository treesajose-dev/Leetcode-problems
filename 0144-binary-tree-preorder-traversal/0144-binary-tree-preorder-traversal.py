class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if root is None:
            return []

        lis = []

        # Root
        lis.append(root.val)

        # Left
        lis = lis + self.preorderTraversal(root.left)

        # Right
        lis = lis + self.preorderTraversal(root.right)

        return lis