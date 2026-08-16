class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S, T = {}, {}
        for char in s:
            S[char] = S.get(char, 0) + 1
        for char in t:
            T[char] = T.get(char, 0) + 1
        return S == T

        