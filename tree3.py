# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
    
    def printNodesAtLevel(self, root:TreeNode, level:int, temp: List[int]) :
        if root is None:
            return
        
        if level == 1:
            temp.append(root.val)
            return
        
        self.printNodesAtLevel(root.left, level - 1, temp)
        self.printNodesAtLevel(root.right, level - 1, temp)
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        res = list()
        max_height = self.getHeight(root)
        for level in range(1, max_height + 1):
            temp = list()
            self.printNodesAtLevel(root, level, temp)
            res.append(temp)
        return res
            
            
            