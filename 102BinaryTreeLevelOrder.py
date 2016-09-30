# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        self.help(root, 0, ans)
        return ans
        
    def help(self, root, level, ans):
        if root:
        	if len(ans)<level+1:
        		ans.append([])
        	ans[level].append(root.val)
        	self.help(root.left, level+1, ans)
        	self.help(root.right, level+1, ans)
