class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        h_s={}
        global_max=0
        for i,v in enumerate(s):
            if v in h_s:
                 h_s[v]=h_s[v]+1
            else:
                h_s[v]=1 
        h_s={k:v for k,v in h_s.items() if v>=2}
        if len(h_s)==0:
            return -1
        
        
        for k,v in h_s.items():
            ls=[i for i, ltr in enumerate(s) if ltr == k]
            local_max=max(ls)-min(ls)
            if local_max>global_max:
                global_max=local_max
                final_ind_max=max(ls)
                final_ind_min=min(ls)
        
        return len(s[final_ind_min+1:final_ind_max])
                