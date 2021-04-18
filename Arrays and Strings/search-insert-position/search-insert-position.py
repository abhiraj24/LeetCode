class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        val=target
        for i,v in enumerate(nums):
            if v==val:
                return i

        if val-nums[len(nums)-1]>=1:
            return  (len(nums))


        elif val-nums[0]<=-1:
            return 0


        else:
            for i in range(0,len(nums)):
                if val-nums[i]>=1 and val-nums[i+1]<=-1:
                    return i+1
                
                
        