class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(0,int(len(s)/2)):
            s[i],s[len(s)-i-1]=s[len(s)-i-1],s[i]
        print(s)

sol=Solution()
sol.reverseString(['h','e','l','l','o'])