class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        e=1
        s=0
        while e<len(nums):
            if nums[s]==nums[e]:
                nums.remove(nums[e])
            else:    
                s+=1
                e+=1
        #num[:]=list(set(nums))
        #num.sort()
        return len(nums)