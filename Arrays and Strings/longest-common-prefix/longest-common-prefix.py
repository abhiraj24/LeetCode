class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        if len(strs)==0:
            return ""
        if strs[0]=="":
            return strs[0]
        
        c=0
        for i in strs:
            if i.startswith(strs[0][0]):
                c+=1
        if c==0:
            return ''
        else:
        
            x=len(strs[0])
    
            for i in range(1,len(strs)):
                if x>len(strs[i]):
                    x=len(strs[i])
                for j in range(0,x):
                    if strs[0][j]==strs[i][j]:
                        continue
                    else:
                        x=j
                        break
            return strs[0][0:x]
        