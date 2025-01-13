class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        
        for element in strs:
            value = "".join(sorted(element))
            result[value].append(element)

        return list(result.values())