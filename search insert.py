class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev_sum = -999
        prev_lst = []
        if len(nums) == 1:
            return nums[0]
        for i in range(0,len(nums)):
            sum = nums[i]
            max_sum = sum
            temp_lst = nums[i:i + 1]
            for j in range(i+1,len(nums)):
                sum = sum + nums[j]
                if max_sum<sum:
                    max_sum = sum
                    temp_lst = nums[i:j+1]
            if prev_sum < max_sum: #or prev_sum < sum:
                prev_sum = max_sum #max(max_sum, sum)
                prev_lst = temp_lst #if max_sum > sum else nums[i:i+1]
            print(prev_lst)
        return prev_sum

print(Solution().maxSubArray([-2,-1]))

