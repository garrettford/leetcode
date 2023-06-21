# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#      def __repr__(self):
#          return f"{self.val}"


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """O(N)TS"""
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """O(N)TS"""

        def left(node):
            while node:
                yield node
                node = node.left

        stack = list(left(root))
        while node := stack.pop() if stack else None:
            yield node.val
            stack += left(node.right)

