class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = float('-inf')
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            best = max(best, curr_sum)

            # if this sum is negative contribution, start anew
            if curr_sum < 0:  
                curr_sum = 0
        return best