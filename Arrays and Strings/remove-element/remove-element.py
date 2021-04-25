class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums=[i for i in nums if i !=val]
        j=0
        for i in nums:
            if i==val:
                continue
            else:
                nums[j]=i
                j+=1
        nums=nums[:j]
        return len(nums)


        