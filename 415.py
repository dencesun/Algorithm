class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)

        if len1 is 0:
        	return num2
        if len2 is 0:
        	return num1

        ans = []
        flag = 0
        while len1 and len2:
        	count = int(num1[len1-1]) + int(num2[len2-1])+flag
        	flag = count/10
        	ans.append(str(count%10))
        	len1 -= 1
        	len2 -= 1
        
        print len1, len2
        if len1 > 0:
        	while len1:
        		count = int(num1[len1-1])+flag
        		flag = count/10
        		ans.append(str(count%10))
        		len1 -= 1
        if len2 > 0:
        	while len2:
        		count = int(num2[len2-1])+flag
        		flag = count/10
        		ans.append(str(count%10))
        		len2 -= 1
        if flag > 0:
        	ans.append(str(flag))
        ans.reverse()
        return "".join(ans)

test = Solution()
print test.addStrings('6','501')
        		
