class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current,gl=nums[0],nums[0]
        if len(nums)==1:
            return nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],current+nums[i])
            
            if current>gl:
                gl=current
        return gl
        
        