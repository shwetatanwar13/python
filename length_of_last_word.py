class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split(' ')
        i = len(l)-1
        while l[i] == '':
           i = i-1
        return len(l[i])

print(Solution().lengthOfLastWord("   fly me   to   the moon  "))
