# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x = 0):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
    	if root != None:
    		# tmp = root.left
    		# root.left = root.right
    		# root.right = tmp
    		root.left, root.right = root.right, root.left
    		self.invertTree(root.left)
    		self.invertTree(root.right)
    	return root

tree = TreeNode(1)
tree1 = TreeNode(2)
tree2 = TreeNode(3)
tree.left = tree1
tree.right = tree2
test = Solution()

test.invertTree(tree)
print tree.left.val, tree.right.val