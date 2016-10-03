# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
# 方法1
        # result = []
        # if root is None:
        # 	return False
        # def dfs(root, ans):
        # 	if root.left is None and root.right is None:
        # 		result.append(ans)
        # 	if root.left:
        # 		dfs(root.left, ans+root.left.val)
        # 	if root.right:
        # 		dfs(root.right, ans+root.right.val)
       	# dfs(root, root.val)
        # if sum in result:
        # 	return True
        # return False
# 方法2
		if root is None: 
			return False
		if root.left is None and root.right is None:
			return root.val == sum
		return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val)

