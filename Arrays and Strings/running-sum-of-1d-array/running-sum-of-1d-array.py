class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=0
        list=[]
        for i in nums:
            sum=sum+i
            list.append(sum)
        return list