from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = defaultdict(list)
        for s in strs:
            S = [0]*26
            for char in s:
                S[ord(char) - ord('a')] += 1

            A[tuple(S)].append(s)
        return list(A.values())

        