class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_dic = {}

        for i,num in enumerate(nums):
            if target - num in num_dic:
                return (i, num_dic[target - num])
            num_dic[nums[i]] = i
        return