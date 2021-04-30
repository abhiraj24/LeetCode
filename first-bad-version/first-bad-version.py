# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        
        """
        if n == 1:
            return 1
        
        left=1
        right=n
        mid=None

        
        while left <= right:
            mid=(left+right)//2
            
            if isBadVersion(mid)==True and isBadVersion(mid-1)==False:
                return mid
            elif isBadVersion(mid)==True and isBadVersion(mid-1)==True:
                right=mid-1
            elif isBadVersion(mid)==False and isBadVersion(mid-1)==False:
                left=mid+1
        
        return -1
                
                