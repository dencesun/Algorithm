# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         lists = list(s)
#         listt = list(t)
#         lists.sort()
#         listt.sort()

#         return lists == listt


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
       	return sorted(s) == sorted(t)

test = Solution()
print test.isAnagram('anagram','nagaram')
print test.isAnagram('rat', 'car')
