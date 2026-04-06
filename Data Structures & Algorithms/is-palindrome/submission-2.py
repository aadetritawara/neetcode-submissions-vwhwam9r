class Solution:
    def isPalindrome(self, s: str) -> bool:
        # space: O(1)
        # time: O(n)

        # initialize left and right pointers
        l = 0
        r = len(s) - 1

        # stop when left pointer exceeds right or both reach the middle
        while l < r:
            # make sure character being compared is alpha numeric
            while l < r and not s[l].isalnum():
                l+=1 
            while r > l and not s[r].isalnum():
                r-=1
            
            if s[l].lower() != s[r].lower():
                return False

            # update left and right pointers
            l, r = l + 1, r - 1
        
        return True