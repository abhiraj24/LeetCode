class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen={}
        for i,v in enumerate(arr):
            if v *2 in seen:
                return True            
            elif v /2 in seen:
                return True
            seen[v]=i
        return False
        