class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        best = 0
        for x in unique:
            if x - 1 not in unique:          # x starts a run
                length = 1
                while x + length in unique:
                    length += 1
                best = max(best, length)
        return best