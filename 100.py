# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
    	if q != None and p != None:
    		if p.val == q.val:
    			ltmp = self.isSameTree(p.left, q.left)
    			rtmp = self.isSameTree(p.right, q.right)
    			return ltmp & rtmp
    		return False
    	elif q == None and p == None:
    		return True
    	else:
    		return False
