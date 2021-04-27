class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        s=list(s)
        while i<len(s):
            s[i:i+k]=s[i:i+k][::-1]
    #print(s)  
            i=2*k+i
        return ''.join(s)
        