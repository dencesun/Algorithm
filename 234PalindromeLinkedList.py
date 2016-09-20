# Definition for singly-linked list.
from copy import deepcopy
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None: return True

        p = head
        l = []
        while p:
        	l.append(p.val)
        	p = p.next
        lr = deepcopy(l)
        lr.reverse()

        return l==lr
    def createNode(self):
    	head = ListNode(0)
    	nums = [1,2,1]

    	for x in nums:
    		p = ListNode(x)
    		p.next = head.next
    		head.next = p
    	return head.next

test = Solution()
head = test.createNode()
print test.isPalindrome(head)