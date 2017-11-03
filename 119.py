class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0 or rowIndex is None:
            return []
        ans = list()
        for n in range(rowIndex+1):
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
        return ans[rowIndex]


rowIndex = 0
test = Solution()
print(test.getRow(rowIndex))