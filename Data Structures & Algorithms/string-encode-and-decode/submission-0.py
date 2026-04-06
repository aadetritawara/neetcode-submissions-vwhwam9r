class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = ""
        for s in strs:
            ret_str += str(len(s)) + "#" + s
        return ret_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0 
        
        while i < len(s):
            j = i
            # find index '#'
            while s[j] != "#":
                j+=1 
            # j is the index of '#', everything before it from i is length int
            word_len = int(s[i:j])
            res.append(s[j + 1 : j + 1 + word_len])
            # character after previous word
            i = j + 1 + word_len
        return res
