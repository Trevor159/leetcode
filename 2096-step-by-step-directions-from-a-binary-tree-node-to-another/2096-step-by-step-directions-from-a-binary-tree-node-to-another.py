# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def getPath(node, val):
            
            if not node:
                return None
            
            if node.val == val:
                return []
            
            rightPath = getPath(node.right, val)
            leftPath = getPath(node.left, val)
            # print(node.val, rightPath, leftPath)
            
            if rightPath is not None:
                rightPath.append("R")
                return rightPath
            
            if leftPath is not None:
                leftPath.append("L")
                return leftPath
            # print(node.val, "cant find", val)
            return None
        # print(root, startValue)
        # print(getPath(root, startValue))
        startPath = getPath(root, startValue)
        destPath = getPath(root, destValue)
        
#         print(startPath)
#         print(destPath)
        
        while startPath and destPath and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()
            
        return "".join(["U"] * len(startPath) + destPath[::-1])