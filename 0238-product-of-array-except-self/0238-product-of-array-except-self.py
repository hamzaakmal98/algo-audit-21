class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = 1
        rp = 1
        ans = [1]*len(nums)

        i = 1 
        while i < len(nums):
            lp *= nums[i-1]
            ans[i] = ans[i] * lp
            i += 1
        
        i = len(nums) -2

        while i > -1:
            rp  *= nums[i+1]
            ans[i] = ans[i] * rp
            i -=1
        
        return ans

            