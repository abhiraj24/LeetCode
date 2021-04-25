class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #gl_sum=0
        #import numpy as np
        #for i in accounts:
        #            gl_sum=max(gl_sum,np.sum(i))
        #    
        #return gl_sum
        res=[]
        for i in accounts:
            res.append(sum(i))
        return max(res)