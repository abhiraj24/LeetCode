class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        
        def isPalin(s,i,j):
            return s[i:j]==s[i:j][::-1]
        
        
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                return isPalin(s,i,j)| isPalin(s,i+1,j+1)
            
            i+=1
            j-=1
        
        return False