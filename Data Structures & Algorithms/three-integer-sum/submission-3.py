class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        for idx in range(n): # fix each number

            target = -1 * sorted_nums[idx]

            # perform 2sum on the remaining array
            ptr1 = idx + 1
            ptr2 = n - 1

            while ptr1 < ptr2: 
                total = sorted_nums[ptr1] + sorted_nums[ptr2]
                if total == target:
                    target_vals = [
                        sorted_nums[idx],
                        sorted_nums[ptr1],
                        sorted_nums[ptr2] 
                        ]
                    res.add(tuple(target_vals))
                    ptr1 += 1
                    ptr2 -= 1
                elif total < target:
                    ptr1 += 1
                else:
                    ptr2 -= 1


        return [list(x) for x in res]
