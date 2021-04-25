class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        s=s.strip()
        
        for i in s:
            if i.isalnum():
                string+=i
        string=string.lower()        
        if string==string[::-1]:
            return True
        else:
            return False
        
        