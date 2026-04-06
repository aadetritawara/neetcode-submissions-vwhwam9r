class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num]+=1
        
        freq_bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in counts.items():
            freq_bucket[freq].append(num)

        res = []
        # traverse backwards
        # backward start index can be exact  
        for i in range(len(freq_bucket) - 1, 0, -1):
            for num in freq_bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
