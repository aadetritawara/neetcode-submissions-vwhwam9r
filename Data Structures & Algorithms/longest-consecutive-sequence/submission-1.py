class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # space: O(n)
        # time: O(n)

        set_nums = set(nums)
        max_seq_length = 0

        for num in set_nums:
            # check if num is start of a seq
            # start means num - 1 doesn't exist in set
            if (num - 1) not in set_nums:
                # determine seq length
                seq_length = 0
                while seq_length + num in set_nums:
                    seq_length += 1
                # update max seq length if current seq longer than current max
                if seq_length > max_seq_length:
                    max_seq_length = seq_length
        return max_seq_length

