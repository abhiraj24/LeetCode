class Solution:
    def findLHS(self, nums: List[int]) -> int:
        best=0
        count=collections.Counter(nums)
        
        for i in count.keys():
            if i+1 in count.keys():
                best=max(best,count[i]+count[i+1])
        return best
        