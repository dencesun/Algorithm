class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # word = str.split()
        # pdict = {}
        # wdict = {}
        # ans = {}
        # if len(pattern) != len(word):
        # 	return False
        # for k, v in zip(pattern, word):
        # 	if k not in pdict:
        # 		pdict[k] = v
        # 	if v not in wdict:
        # 		wdict[v] = k
        # 	if pdict[k] != v or wdict[v]!=k:
        # 		return False
        # return True

        # 方法2
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        return map(pattern.find, pattern) == map(words.index, words)

