class Solution(object):
    def deleteNode(self, node):
    	if node == None:
    		return
    	node.val = node.next.val
    	node.next = node.next.next
