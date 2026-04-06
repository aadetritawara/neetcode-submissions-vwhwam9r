class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            check_num = target - num
            if check_num in seen:
                return [seen[check_num], i]
            seen[num] = i
