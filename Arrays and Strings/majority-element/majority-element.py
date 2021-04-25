class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #solution:1
        #seen={}
        #cnt=1
        #for i in range(len(nums)):
        #    if nums[i] in seen:
        #        seen[nums[i]]=seen[nums[i]]+1
        #    else:
        #        seen[nums[i]]=cnt
        #for key, value in seen.items():  
        #    if value == max(seen.values()):
        #        return key
        
        #Solution 2
        count=0
        max_element=0
        
        for i in range(len(nums)):
            if count==0:
                max_element=nums[i]
            if nums[i]==max_element:
                count+=1
            else:
                count-=1
        return max_element
        
                