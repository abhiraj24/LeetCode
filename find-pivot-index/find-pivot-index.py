class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #arr=[1,2,3]
        i=0
        index=-1
        while i<len(nums):
            #print(sum(arr[:i]))
            #print(sum(arr[i+1:]))
            if sum(nums[:i])==sum(nums[i+1:]):
                index=i
                break
            i+=1
        return index