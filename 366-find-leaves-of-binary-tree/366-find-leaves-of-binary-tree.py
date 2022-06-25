# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        def processNode(node):
            
            if not node:
                return -1
            
            leftHeight = processNode(node.left)
            rightHeight = processNode(node.right)
            
            height = max(leftHeight, rightHeight) + 1
                
            if len(ans) == height:
                ans.append([])
                
            ans[height].append(node.val)
            
            return height
            
        processNode(root)
        return ans