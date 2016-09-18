# # Definition for singly-linked list.
# # class ListNode(object):
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         head = ListNode(0)
#         r = head
#         p = l1
#         q = l2
#         while p!=None and q!=None:
#         	if p.val < q.val:
#         		r.next = p
#         		r = p
#         		p = p.next
#         	else:
#         		r.next = q
#         		r = q
#         		q = q.next
#         if p!=None:
#         	r.next = p
#         elif q!=None:
#         	r.next = q
#         return head.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val < l2.val:
        	ret = l1
        	ret.next = self.mergeTwoLists(l1.next, l2)
        else:
        	ret = l2
        	ret.next = self.mergeTwoLists(l1, l2.next)
        return ret




















