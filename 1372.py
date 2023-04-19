# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        self.streak = 0

        def recurse(self, node, lor, stk):

            self.streak = max(self.streak, stk)
            if node.left != None:
                if lor == 'r':
                    recurse(self, node.left, 'l', stk + 1)
                else:
                    recurse(self, node.left, 'l', 1)

            if node.right != None:
                if lor == 'l':
                    recurse(self, node.right, 'r', stk + 1)
                else:
                    recurse(self, node.right, 'r', 1)

        
        recurse(self, root, 'o', 0)

        return self.streak