class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return strs[0][0:i]
        return strs[0]        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans = ""
        # if not strs:
        #     return ans
        
        # min_len = float("inf")
        # for word in strs:
        #     min_len = min(min_len,len(word))
     
        # for i in range(min_len):
        #     pre = strs[0][i]
        #     for word in strs:
        #         if word[i] != pre:
        #             return strs[0][0:i]
        # return strs[0][0:min_len]
        