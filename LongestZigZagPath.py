# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], length: int, isLeft: bool) -> int:
            if not node:
                return length

            left_length = dfs(node.left, length + 1, False)
            right_length = dfs(node.right, 1, True)


            left_length_alt = dfs(node.left, 1, False)
            right_length_alt = dfs(node.right, length + 1, True)

            return max(left_length, right_length, left_length_alt, right_length_alt)
        return max(dfs(root.left, 1, False), dfs(root.right, 1, True)) - 1
