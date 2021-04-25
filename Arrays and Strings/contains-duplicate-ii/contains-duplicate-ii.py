class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen={}
        for i,v in enumerate(nums):
            if v not in seen:
                seen[v]=i
            else:
                idx_diff = abs(i - seen[v])
                if idx_diff <= k:
                    return True
                else: 
                    seen[v] = i
        return False     