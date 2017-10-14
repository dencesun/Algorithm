class Solution(object):
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     max = ''
    #     lens = len(s)

    #     for i in range(lens):
    #     	for j in range(i+1,lens+1):
    #     		# print j
    #     		substr = s[i:j]
    #     		if len(substr)>len(max):
    #    				if self.isPalindrome(substr):
    #     				max = substr
    #     return max

    # def isPalindrome(self, l):
    # 	lens = len(l)
    # 	flag = True
    # 	for i in range(lens/2):
    # 		if l[i] != l[lens-i-1]:
    # 			flag = False
    # 			break
    # 	return flag
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
    	lens = len(s)
    	max = ''
    	for i in range(lens):
    		substr = self.getlongestPalindrome(s, i,i)
    		if len(max)<len(substr):
    			max = substr
    		substr = self.getlongestPalindrome(s,i,i+1)
    		if len(max)<len(substr):
    			max = substr
    	return max
    def getlongestPalindrome(self, s, l,r):
    	while l>=0 and r<len(s) and s[l] == s[r]:
    		l -= 1
    		r += 1
    	return s[l+1:r]
test = Solution()
print test.longestPalindrome('aaabbbbaaa')
