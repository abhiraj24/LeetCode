class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h_r={}
        h_m={}

        for i,v in enumerate(ransomNote):
            if v in h_r:
                 h_r[v]=h_r[v]+1
            else:
                h_r[v]=1 
        for i,v in enumerate(magazine):
            if v in h_m:
                 h_m[v]=h_m[v]+1
            else:
                h_m[v]=1 
                
        used_letters=[k for k,v in h_r.items() if k in h_m]
        not_used=[k for k,v in h_r.items() if k not in h_m]
        if ransomNote=="" and magazine=="":
            return True
        
        if ransomNote=="" and len(magazine)!=0:
            return True 
        
        if used_letters==[] or len(not_used)>0:
            return False
        
        else:
            for i in used_letters:
                if h_r[i]<=h_m[i]:
                    continue
                else:
                    return False
                    break
            
            return True
        