class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        else:
            largest=max(nums)
            larg_index=nums.index(largest)
            nums=[val for val in nums if val!=largest]
            for i in nums:
                if largest>=2*i:
                    continue
                else:
                    return -1
            return larg_index
        