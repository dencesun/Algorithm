# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.preorder(root, ans)
        return ans

    def preorder(self, root, ans):
    	if root:
    		ans.append(root.val)
    		self.preorder(root.left, ans)
    		self.preorder(root.right,ans)

    	return ans
