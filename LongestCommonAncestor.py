class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or equal to either p or q, return root
        if not root or root in (p, q):
            return root

        # Recursively search in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right subtrees return a node, root is the LCA
        if left_lca and right_lca:
            return root

        # If one subtree returns None, return the non-None result
        return left_lca or right_lca
