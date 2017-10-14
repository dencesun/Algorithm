import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
    	ransomNotelist = list(ransomNote)
    	magazinelist = list(magazine)
    	flag = True
    	for ran in ransomNotelist:
    		if ran in magazinelist:
    			magazinelist.remove(ran)
    			flag = True
    		else:
    			return False
    	return flag

# method2

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         cnt = collections.Counter(magazine)
#         for letter in ransomNote:
#             cnt[letter] -= 1
#             if cnt[letter] <0: return False
#         return True
test = Solution()
print test.canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi")
