class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for char in address:
            if char != ".":
                ans += char
            else:
                ans = ans + "[.]"
        return ans