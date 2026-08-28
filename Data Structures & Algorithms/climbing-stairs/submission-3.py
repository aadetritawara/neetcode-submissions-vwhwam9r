class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        M = [0] * (n+1)
        M[1] = 1
        M[2] = 2
        
        for i in range(3, n+1):
            M[i] = M[i - 1] + M[i - 2]
        return M[n]
