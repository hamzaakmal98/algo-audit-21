class Solution:
    def reorderSpaces(self, text: str) -> str:
        
        nspaces = text.count(" ")
        
        words = text.split()
        nwords = len(words)
        
        if nwords == 1:
            return words[0] + " " * nspaces
        
        space_between = nspaces // (nwords - 1)
        space_remaining = nspaces % (nwords - 1)
        
        return (" " * space_between).join(words) + " " * space_remaining