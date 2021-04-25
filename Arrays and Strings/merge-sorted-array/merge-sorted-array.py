class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #suboptimal
        #nums1[m:]=nums2[:]
        #nums1.sort()
        
#       #optimal
#       k=m+n-1
#       m,n=m-1,n-1
#       while k>=0 :#and m>=0 and n>=0:

#           if m<0:
#               nums1[k]=nums2[n]
#               n-=1
#               k-=1
#           elif n<0 :
#               nums1[k]=nums1[m]
#               m-=1
#               k-=1
#               #break

#           if(nums1[m]<=nums2[n]):
#               nums1[k]=nums2[n]
#               n-=1
#               k=-1

#           elif(nums1[m]>nums2[n]):
#               nums1[k]=nums1[m]
#               m-=1
#               k-=1
#          # k-=1
#       
        i=m-1
        j=n-1
        k=n+m-1
        while k>=0:
            
            if j <0:
                nums1[k]=nums1[i]
                i-=1
                k-=1
            elif i <0:
                nums1[k]=nums2[j]
                j-=1
                k-=1
            else:
                if nums1[i] <= nums2[j]:
                    nums1[k]=nums2[j]
                    j-=1
                    k-=1
                else:
                    nums1[k]=nums1[i]
                    i-=1 
                    k-=1
