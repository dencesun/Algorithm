class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0 or numRows is None:
            return []
        ans = list()
        for n in range(numRows):
            tmp = list([0])*(n+1)
            if n == 0:
                ans.append([1])
                continue
            tmp[-1], tmp[0] = 1, 1
            for i in range(n+1):
                if i == 0 or i == n:
                    continue
                tmp[i] = ans[n-1][i-1] + ans[n-1][i]
            ans.append(tmp)
        return ans


nums = 5
test = Solution()
print(test.generate(5))
