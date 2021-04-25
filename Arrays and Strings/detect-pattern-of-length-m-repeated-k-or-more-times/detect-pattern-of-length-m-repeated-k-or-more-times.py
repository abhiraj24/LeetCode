class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        i=0
        while i<len(arr)-1:
            a=arr[i:i+m]
            if a*k==arr[i:i+m*k]:
                return True
            i+=1
        return False
        