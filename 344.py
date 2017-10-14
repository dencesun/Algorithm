class Solution(object):
    def reverseString(self, s):
        strlen = len(s)
        s = list(s)
        for i in range(strlen/2):
        	tmp = s[i]
        	s[i] = s[strlen-i-1]
        	s[strlen-i-1] = tmp

        return ''.join(s)

# class Solution(object):
# 	def reverseString(sefl, s):
# 		return s[::-1]

test = Solution()

print test.reverseString('hello')
