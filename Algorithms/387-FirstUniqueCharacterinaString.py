class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        s = list(s)
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = [i]
            else:
                chars[s[i]].append(i)
        first = -1
        for key, value in chars.iteritems():
            if len(value) == 1 and (value[0] < first or first == -1):
                first = value[0]
        return first
