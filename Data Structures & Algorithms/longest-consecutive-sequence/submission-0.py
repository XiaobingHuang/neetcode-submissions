class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums:
            if num -1 not in nums_set:
                cur = num
                count = 1
                while cur+1 in nums_set:
                    count += 1
                    cur = cur + 1
                longest = max(longest, count)
        return longest

        

        