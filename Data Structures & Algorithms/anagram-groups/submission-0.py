class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # if key doesn't exist, add it with a default value of list
        out_dict = defaultdict(list) # mapping 26-length tuple: [anagrams]
        
        for word in strs:
            # create empty key representing character frequency
            char_freq = [0]*26

            for char in word:
                # increment appropriate indices for the word
                char_freq[ord(char) - ord("a")]+=1

            out_dict[tuple(char_freq)].append(word)
        
        return list(out_dict.values())