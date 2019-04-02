class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d=dict()
        for i in nums:
            if i in d.keys():
                return(True)
            else:
                d[i]=1
        return(False)

s=Solution()
print(s.containsDuplicate([]))