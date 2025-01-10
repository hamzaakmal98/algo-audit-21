class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        mc = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            mc = max(mc, r + 1 - l)
            seen.add(s[r])
        return mc
                



        # seen = set()
        # count = 0
        # mc = 0
        # l = 0
        # r = 0
        # while r < len(s):
        #     if s[r] not in seen:
        #         count += 1
        #         mc = max(count,mc)
        #         seen.add(s[r])
        #         r += 1
        #     else:
        #         l += 1
        #         r = l
        #         seen = set()
        #         count = 0
        # return mc
            
        