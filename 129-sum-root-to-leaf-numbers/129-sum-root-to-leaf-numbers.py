# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        ans = 0
        
        stack = [(root, 0)]
        
        while stack:
            node, val = stack.pop()
            
            val = val * 10 + node.val
            if not node.left and not node.right:
                ans += val
                
            if node.left:
                stack.append((node.left, val))
                
            if node.right:
                stack.append((node.right, val))
                
        return ans
        
        
        
        