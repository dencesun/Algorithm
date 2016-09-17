# class Solution(object):
#     def climbStairs(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n == 1: return 1
#         if n == 2: return 2
#         return self.climbStairs(n-1)+self.climbStairs(n-2)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return n
        cache = [0 for i in range(n)]
        cache[0] = 1
        cache[1] = 2
        for x in range(2,n):
        	cache[x] = cache[x-1]+cache[x-2]
        return cache[n-1]

test = Solution()
print test.climbStairs(35)







