class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_len=len(s)
        i=1
        
        while i <s_len:
            substring=s[0:i]
            factor=int(len(s)/len(substring))
            if(substring*factor==s):
                return True
            i+=1
        return False
            
        