class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ls=s.split(' ')
        seen={}
        if len(ls) != len(pattern):
            return False
        
        
        for p,w in zip(pattern,ls):
            if p not in seen and w not in seen.values():
                seen[p]=w

            elif p not in seen or seen[p]!=w:
                return False
        
        return True       