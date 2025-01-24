class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = defaultdict(int)
        maxn = -1
        for num in arr:
            dic[num] += 1
        for num, freq in dic.items():
            if num == freq:
                maxn = max(maxn, num)
        return maxn