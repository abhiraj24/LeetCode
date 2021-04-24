class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return nums
        if len(nums)==1:
            return [str(nums[0])]
        
        start=nums[0]
        end=None
        i=0
        r=[]
        while i<len(nums)-1:
            if nums[i]+1==nums[i+1]:
                i=i+1
                continue
            else:
                end=nums[i]
                if start==end:
                    r.append(f"{start}")
                else:
                    r.append(f"{start}->{end}")
                i=i+1
                start=nums[i]
                    
        if nums[i]==start:
                r.append(f"{start}")
        else:
                r.append(f"{start}->{nums[i]}")
        return r
                
                