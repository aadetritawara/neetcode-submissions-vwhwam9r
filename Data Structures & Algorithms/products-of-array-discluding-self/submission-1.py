class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # traverse forward & create prefix list
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # update prefix
        
        # traverse backwards & multiply prefix * suffix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
