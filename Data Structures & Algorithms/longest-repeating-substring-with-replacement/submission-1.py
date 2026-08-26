class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        MAX = 0
        l = 0
        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            n = max(chars.values())
            while (r-l+1) - n > k:
                chars[s[l]] -= 1
                l += 1
                
            MAX = max(MAX, r-l+1)
        return MAX
            
            



        