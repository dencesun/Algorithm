# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         tmp = {}
#         flag = 0
#         for x in prices:
#         	index = prices.index(x)+1
#         	tmp[x]=[p-x for p in prices[index:len(prices)]]
        	
#         	max=sorted(tmp[x], reverse=True)
#         	if len(max)>0 and max[0]>flag:
#         		flag = max[0]
#         return flag

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         flag = 0
#         for x in prices:
#         	for p in prices[prices.index(x)+1:len(prices)]:
#         		if (p-x)>flag:
#         			flag = p-x
#        	return flag
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<2: return 0
        min_price = prices[0]
        max_profit = 0
        for x in prices:
        	if min_price>x:
        		min_price=x
        	if x-min_price > max_profit:
        		max_profit = x-min_price
        return max_profit

test = Solution()
print test.maxProfit([7,1,5,3,4,6])