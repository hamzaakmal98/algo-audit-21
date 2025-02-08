class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in jewels:
            for i in range(len(stones)):
                if stones[i] == char:
                    count += 1
        return count