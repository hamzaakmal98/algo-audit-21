class Solution:
    def reformat(self, s: str) -> str:
        num = 0
        let = 0
       
        if len(s) == 1:
            return s
        
        for char in s:
            if char.isdigit():
                num += 1
            if char.isalpha():
                let += 1

        if abs(num - let) > 1:
            return ""    

        if num >= let:
            n = 0
            l = 1
        else:
            n = 1
            l = 0
        
        ans = [0] * len(s)
        
        for char in s:
            if char.isdigit():
                ans[n] = char
                n += 2
            else:
                ans[l] = char
                l += 2
        
        return ''.join(ans)
