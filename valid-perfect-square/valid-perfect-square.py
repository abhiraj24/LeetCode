class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        left=1
        right=num
        ans=1
        while left<=right:
            mid=(left+right)//2
            if mid*mid<=num:
              ans=mid
              left=mid+1
        
            elif mid*mid>num:
              right=mid-1
              
        return ans*ans==num
        