# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
        	return 0
        else:
        	return max(self.maxDepth(self, root.right), self.maxDepth(root.left)) + 1

# tree=['A',['B',['D',[],[]],['E',[],[]]],['C'，['F',[],[]],[]]]

# def BinaryTree(item):
# 	return [item, [], []]

# def insertLeft(tree, item):
# 	leftSubtree = tree.pop(1)
# 	if leftSubtree:
# 		tree.insert(1,[item, leftSubtree, []])
# 	else:
# 		tree.insert(1, [item, [], []])
# 	return tree

























