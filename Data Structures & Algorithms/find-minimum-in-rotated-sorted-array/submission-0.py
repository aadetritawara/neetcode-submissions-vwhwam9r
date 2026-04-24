class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf') # initialize as big value
        l, r = 0, len(nums) - 1
        while (l <= r):
            mid = (r + l) // 2

            # already sorted
            if nums[r] >= nums[l]:
                return min(nums[l], res)

            # if not sorted but left portion sorted
            if nums[mid] >= nums[l]:
                res = min(res, nums[l])
                # update to search right portion
                l = mid + 1
            else:
                # check left portion
                r = mid
        return res
