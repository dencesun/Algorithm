# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None: return None

        while head!=None and head.val == val:
            head = head.next
        if head == None: return head

        p = head
        while p:
            if p.next!=None and p.next.val == val:
                p.next = p.next.next
            elif p!=None:
                p = p.next
        return head

node = ListNode(1)
# nums = [2,6,3,4,5,6]

# r = node

# for x in nums:
# 	p = ListNode(x)
# 	r.next = p
# 	r = p

test = Solution()
r = test.removeElements(node, 2)

while r:
	print r.val
	r = r.next










