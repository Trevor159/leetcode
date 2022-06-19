class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        left = right = 0
        N = len(s)
        total = 0
        ans = 0
        binary = bin(k)[2:]
        index = len(binary)-1
        greater = False
        for c in reversed(s):
            if index > 0:
                if c > binary[index]:
                    greater = True
                elif c < binary[index]:
                    greater = False
                index -= 1
                ans += 1
            elif index == 0:
                if not greater or c == "0":
                    index -= 1
                    ans += 1
            elif c == "0":
                ans += 1
        return ans