class Solution(object):
    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #   	l = []

    #   	for i in s:
    #   		if i is '(' or i is '[' or i is '{':
    #   			l.append(i)
    #   		if i is ')' and len(l)>0 and l[-1] is '(':
    #   			l.pop()
    #    		if i is ']' and len(l)>0 and l[-1] is '[':
    #   			l.pop()
    #   		if i is '}' and len(l)>0 and l[-1] is '{':
    #   			l.pop()

    #   	if len(l)>0:
    #   		return False
    #   	return True

    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True
            
test = Solution()
print test.isValid("()")
