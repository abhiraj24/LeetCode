class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        import math
        s = [str(i) for i in digits]
        total = int("".join(s))
        total=total+1
    
        rem=[]
        while total!=0:
            q, r = divmod(total,10)
            total=q
            rem.append(r)
        rem=rem[::-1]
        return [int (x) for x in rem]

        