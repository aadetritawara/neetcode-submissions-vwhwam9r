
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # time: O(n), space: O(n)
        
        longest_substring = 0
        l = 0
        seen = set()

        for r in range(len(s)):
            # if right pointer value in seen, increment left until no longer in seen
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        return longest_substring