class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(n^2)
        res = list() 
        nums.sort() # so that all duplicates appear in the same order
        for i, a in enumerate(nums):
            # if not the first index and is duplicate of prev val
            if i != 0 and a == nums[i - 1]:
                continue 
            
            # two sum problem over remaining nums
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                elif threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-+1
                    # update left pointer if same value as prev
                    # to prevent duplicates in results
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        return res

