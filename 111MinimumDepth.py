# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        # 方法1
        # ans = []
        # if root is None:
        # 	return 0
        # def dfs(root, depth):
        # 	if root.right is None and root.left is None:
        # 		ans.append(depth+1)
        # 	if root.left is not None:
        # 		dfs(root.left, depth+1)
        # 	if root.right is not None:
        # 		dfs(root.right, depth+1)
       	# dfs(root, 0)
       	# ans.sort()
       	# print ans
       	# return ans[0]

       	# 方法2
      	if root is None: return 0
      	if root.left is None and root.right is not None:
      		return self.minDepth(root.right)+1
      	if root.left is not None and root.right is None:
      		return self.minDepth(root.left)+1
      	return min(self.minDepth(root.left), self.minDepth(root.right))+1