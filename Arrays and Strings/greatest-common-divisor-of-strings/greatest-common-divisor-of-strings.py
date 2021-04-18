class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
    #    if not str1:return str2
    #    if not str2:return str1
    #    
    #    str1,str2=(str1,str2) if len(str1)<=len(str2) else(str2,str1)
    #    
    #    if str1[:len(str2)]==str2:
    #        return self.gcdOfStrings(str1[len(str2):],str2)
    #    return ''
    
   #class Solution:
   #def gcdOfStrings(self, s: str, t: str) -> str:
        s=str1
        t=str2
        if not s: return t
        if not t: return s
        s, t = (s, t) if len(s) <= len(t) else (t, s)
        if t[:len(s)] == s:
            return self.gcdOfStrings(t[len(s):], s)
        return ''