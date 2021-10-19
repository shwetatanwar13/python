class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        print( str(n))
        for i in str(n):
            print(i)
            if i == '1':
              count = count+1
        return count

print(Solution().hammingWeight('00000000000000000000000000001011'))
