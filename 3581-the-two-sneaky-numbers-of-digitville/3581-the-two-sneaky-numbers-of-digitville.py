class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = defaultdict(int)
        ans = []
        for i in nums:
            c[i] += 1
            if c[i] == 2:
                ans.append(i)
        return ans