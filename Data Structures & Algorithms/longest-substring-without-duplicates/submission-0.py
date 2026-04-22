
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force: O(n^2)
        longest_substring = 0

        for i in range(len(s)):
            seen = []  # reset for each starting point
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.append(s[j])
                    longest_substring = max(longest_substring, len(seen))
                else:
                    break  # stop this substring when duplicate found

        return longest_substring
                    


            
            

        return longest_substring
