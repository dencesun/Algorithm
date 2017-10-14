# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = 0
        len2 = 0
        cl1 = l1
        cl2 = l2

        # while cl1:
        #     len1 += 1
        #     cl1= cl1.next

        # while cl2:
        #     len2 += 1
        #     cl2 = cl2.next
        len1 = self.computelen(l1)
        len2 = self.computelen(l2)
        if len1 < len2:
            # cl1 = l1
            # while cl1:
            #     if cl1.next is None:
            #         break
            #     cl1 = cl1.next
            # for i in range(len2-len1):
            #     cl1.next = ListNode(0)
            #     cl1 = cl1.next
            self.addnum(l1, len2-len1, 0)
        if len1 > len2:
            # cl2 = l2
            # while cl2:
            #     if cl2.next is None:
            #         break
            #     cl2 = cl2.next
            # for i in range(len1-len2):
            #     cl2.next = ListNode(0)
            #     cl2 = cl2.next
            self.addnum(l2, len1-len2, 0)
        cl1 = l1
        cl2 = l2
        flag = 0
        while cl1:
            count = cl1.val + cl2.val + flag
            cl1.val = count % 10
            flag = count/10
            cl1 = cl1.next
            cl2 = cl2.next
        if flag > 0:
            # cl1 = l1
            # while cl1:
            #     if cl1.next is None:
            #         cl1.next = ListNode(flag)
            #         break
            #     cl1 = cl1.next
            self.addnum(l1, 1, flag)
        return l1

    def computelen(self, head):
        l = head
        lens = 0
        while l:
            lens += 1
            l = l.next
        return lens
    def addnum(self, head, count, num):
        l = head
        while l:
            if l.next is None:
                break
        for i in range(count):
            l.next = ListNode(num)
            l = l.next
