class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_str = "".join(char.lower() for char in s if char.isalnum())

        # find reversed string
        reversed_str = alphanum_str[::-1]

        return reversed_str == alphanum_str
