# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        i = 0
        while p:
        	if i%2 == 0 and p.next !=None:
        		p.val, p.next.val = p.next.val, p.val
        	i+=1
        	p=p.next
        return head

head = ListNode(1)
r = head
nums = [2,3,4]
for x in nums:
	node = ListNode(x)
	r.next = node
	r = node
test = Solution()

p = test.swapPairs(head)
while p:
	print p.val
	p = p.next