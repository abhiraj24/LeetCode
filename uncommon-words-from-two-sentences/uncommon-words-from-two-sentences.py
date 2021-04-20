class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
       
        A_set=A.split(' ')
        B_set=B.split(' ')
        
        h_a={}
        h_b={}
        final_list=[]
        
        for i,v in enumerate(A_set):
            if v in h_a:
                 h_a[v]=h_a[v]+1
            else:
                h_a[v]=1
                
        for i,v in enumerate(B_set):
            if v in h_b:
                 h_b[v]=h_b[v]+1
            else:
                h_b[v]=1        
        
        A_common=[k for k,v in h_a.items() if v>1]
        B_common=[k for k,v in h_b.items() if v>1]
        
        A_ls=[]
        B_ls=[]
        
        for i in A_set:
            if i not in A_common and i not in B_set:
                A_ls.append(i)
        
        for i in B_set:
            if i not in B_common and (i not in A_set):
                B_ls.append(i)
        return A_ls+B_ls

                
        
        