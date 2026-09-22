class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashe = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            hashe[key].append(s)
            
        return list(hashe.values())