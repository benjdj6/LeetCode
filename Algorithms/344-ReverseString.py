# In python the -1 element of a list is the last element
# So to reverse a string you can simply go from -1 backwards

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[-1::-1]