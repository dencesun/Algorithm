#!/bin/usr/env python
# -*- coding: utf-8 -*-
# class Solution(object):
#     def singleNumber(self, nums):
#     	nums = sorted(nums)

#     	for i in range(0,len(nums)-1, 2):
#     		if nums[i] != nums[i+1]:
#     			return nums[i]
#         return nums[-1]

#利用^进行计算
class Solution(object):
    def singleNumber(self, nums):
    	ans = nums[0]
    	for i in range(1,len(nums)):
    		ans ^= nums[i]
    	return ans
test = Solution()

print test.singleNumber([1,2,2])
