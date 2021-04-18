class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,v in enumerate(numbers):
            if (target-v) in seen:
                return [seen[(target-v)]+1,i+1]
            seen[v]=i
        