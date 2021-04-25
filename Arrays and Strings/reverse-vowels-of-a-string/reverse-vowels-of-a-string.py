class Solution:
    def reverseVowels(self, s: str) -> str:
        vo='aeiouAEIOU'
        in_1=[]
        val_1=[]
         
        s1=[]
        s1[:0]=s
        for i,v in enumerate(s1):
             if v in vo:
                in_1.append(i)
                val_1.append(v)
                
        val_1.reverse()
            
        for k,i in enumerate(in_1):
             s1[i]=val_1[k] 
        
        return ''.join(s1)