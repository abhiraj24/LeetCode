class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        leng=len(nums)
        max_ele=max(nums)
        if max_ele!=1:
            ls=[i for i in range(1,leng+1)]
        else:
            ls=[max_ele,max_ele+1]
        h_s={}

        for i,v in enumerate(nums):
            if v in h_s:
                h_s[v]=h_s[v]+1
            else:
                h_s[v]=1
        elements=[k for k,v in h_s.items() if v==2 ]+[i for i in ls if i not in nums]
        return elements
                            

        
        
        