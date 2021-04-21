class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0
        e=1
        count=[]
        if len(nums)==1:
            return 0
        
        while e<len(nums):
            if nums[i]>=nums[e]:
                diff=nums[i]-nums[e]
                nums[e]+=diff+1
                count.append(diff+1)

            i=e
            e+=1
        return sum(count)

        