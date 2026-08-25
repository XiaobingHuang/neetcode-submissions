class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        MAX = 0
        l = 0
        comb = set()
        for r in range(len(s)):
            while s[r] in comb:
                comb.remove(s[l])
                l += 1
            comb.add(s[r])
            MAX = max(MAX, r-l+1)
        return MAX



        