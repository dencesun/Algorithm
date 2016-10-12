class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
      	l = []

      	for i in s:
      		if i is '(' or i is '[' or i is '{':
      			l.append(i)

      		if i is ')' and l and l.pop() !='(':
      			return False
       		if i is ']' and len(l)>0 and l[-1] is '[':
      			l.pop()
      		if i is '}' and len(l)>0 and l[-1] is '{':
      			l.pop()

      	if len(l)>0:
      		return False
      	return True

test = Solution()
print test.isValid("[")