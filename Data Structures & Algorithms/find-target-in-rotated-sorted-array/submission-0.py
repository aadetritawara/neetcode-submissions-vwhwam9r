class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            # If target found at mid return index 
            if nums[mid] == target:
                return mid

            # LEFT portion sorted?
            if nums[l] <= nums[mid]:
                # Is the target INSIDE sorted left portion?
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1  # search left
                else:
                    l = mid + 1  # search right
            
            # LEFT unsorted = RIGHT portion sorted
            else:
                # Is the target INSIDE sorted right portion?
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1  # search right
                else:
                    r = mid - 1  # search left

        # if loop finishes without target found, it's not in nums
        return -1

