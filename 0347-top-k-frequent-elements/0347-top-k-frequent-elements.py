class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        result = []

        for num in nums:
            count[num] += 1

        sorted_arr = sorted(count.items(), reverse = True, key = lambda item: item[1])

        for item in sorted_arr[:k]:
            result.append(item[0])
        
        return result
