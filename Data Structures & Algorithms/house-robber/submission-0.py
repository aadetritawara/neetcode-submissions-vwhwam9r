class Solution:
    def rob(self, nums: List[int]) -> int:
        # either rob the current house: nums[i] + M[i - 2]
        # or don't rob the current house: M[i - 1]

        # base case: if no house, max amount is $0
        if len(nums) == 0:
            return 0
            
        M = [0]*(len(nums) + 1)

        # base case: if only one house, it has the max $
        M[1] = nums[0]

        for i in range(2, len(nums) + 1):
            curr_idx = i - 1

            M[i] = max(nums[curr_idx] + M[i - 2], M[i - 1])
        
        return M[len(nums)]


        

