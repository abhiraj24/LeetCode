class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """
        k=0
        e=len(s)-1
        while k<e:
            swap1=s[k]
            swap2=s[e]
            s[k]=swap2
            s[e]=swap1
            k+=1
            e-=1
        return s