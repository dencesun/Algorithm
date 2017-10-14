#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        if len(v1)<len(v2):
        	v1.extend([0]*(len(v2)-len(v1)))
        else:
        	v2.extend([0]*(len(v1)-len(v2)))
        return cmp(v1,v2)


# test = Solution()
# print test.compareVersion('0.01.0.1', '0.0.1')

# map补充

class mapLearn(object):
	def add100(self, x):
		return x+100
	def abc(self, a, b, c):
		return a*10000+b*100+c
	def test(self):
		list1 = [11,22,33]
		list2 = [44,55,66]
		list3 = [77,88,99]
		print map(self.add100, list1)
		print map(self.abc, list1, list2, list3)
		print map(None, list1, list2, list3)
test = mapLearn()
test.test()

