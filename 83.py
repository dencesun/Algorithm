# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplicates(self, head):
        if head==None or head.next==None:
            return head
       	p = head
       	cur = p.next
       	while cur:
       		if p.val == cur.val:
       			p.next = cur.next
       			cur = cur.next
       		else:
       			p = cur
       			cur = cur.next
       	return head

l = [1,2,2,3]
head = ListNode(0)
tmp = head
for x in l:
	q = ListNode(x)
	tmp.next = q
	tmp = q

test = Solution()
head= test.deleteDuplicates(head)
while head:
	print head.val
	head = head.next
