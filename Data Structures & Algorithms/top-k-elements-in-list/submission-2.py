from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = defaultdict(int)
        ans = []
        for num in nums:
            A[num] += 1
        
        for key, count in A.items():
            ans.append([count, key])
        ans.sort()
        

        res = []
        while len(res) < k:
            res.append(ans.pop()[1])
        return res


        