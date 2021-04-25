class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count=1
        count=1
        if len(set(nums))==1:
            return 1
        
        if len(nums)==0:
            return 0
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                count=1
            if count>max_count:
                max_count=count
        return max_count
        