class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums))<=2:
            return max(nums)
        else:
            m,s,t=-math.pow(2,31),-math.pow(2,31),-math.pow(2,31)
            seen={}
            for i,V in enumerate(nums):
                if V>=m and V not in seen:
                    t=int(s)
                    s=int(m)
                    m=int(V)
                elif V>=s and V not in seen:
                    t=int(s)
                    s=int(V)
                elif V>=t and V not in seen:
                    t=int(V)
                seen[V]=i

        return t
            
        