class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the deduplicated array
        sorted_nums = sorted(set(nums)) #O(n*logn)
        res_nums = list()
        max_seq = 0
        for i in range(len(sorted_nums)): # O(n)
            curr = sorted_nums[i]
            next_seq = curr + 1
            res_nums.append(curr)

            # If sequence stops here, reset res_nums
            # Replace max_seq if current sequence was longer
            if (i + 1) != len(sorted_nums) and sorted_nums[i+1] != next_seq:
                if max_seq < len(res_nums):
                    max_seq = len(res_nums)
                res_nums = list()
            if (i + 1) == len(sorted_nums):
                if max_seq < len(res_nums):
                    max_seq = len(res_nums)
        return max_seq

