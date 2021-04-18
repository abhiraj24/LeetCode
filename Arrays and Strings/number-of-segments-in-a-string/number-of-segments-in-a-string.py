class Solution:
    def countSegments(self, s: str) -> int:
        if s=="" or s ==" ":
            return 0
        elif len(s)==1:
            return 1
        ls=s.split(' ')
        return len([i for i in ls if i not in ""])
        