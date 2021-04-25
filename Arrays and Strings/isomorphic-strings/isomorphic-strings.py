class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen={}
        for p,w in zip(s,t):
            if p not in seen and w not in seen.values():
                seen[p]=w

            elif p not in seen or seen[p]!=w:
                return False
        return True
        