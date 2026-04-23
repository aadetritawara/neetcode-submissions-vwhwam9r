class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {
            '(': ')', 
            '{': '}',
            '[': ']'
            }

        # push into stack until opposite bracket seen, then pop
        for string in s:
            print(stack)
            if string in matches.keys():
                stack.append(string)
            else:
                if not stack:
                    return False
                res = stack.pop()
                if matches[res] != string:
                    return False
        return len(stack) == 0