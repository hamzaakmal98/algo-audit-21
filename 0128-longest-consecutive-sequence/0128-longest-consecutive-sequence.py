class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        max_length = 1
        nums_set = set(nums)

        for element in nums_set:
            if element - 1 not in nums_set:
                length = 0
                while element + length in nums_set:
                    length += 1
                    max_length = max(max_length, length)
        
        return max_length

