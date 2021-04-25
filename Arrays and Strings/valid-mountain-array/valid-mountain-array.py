class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
           if len(arr)<3:
               return False
           m=max(arr)
           ind=arr.index(m)
           
           if ind==0 or ind==len(arr)-1:
               return False
           
           for i in range(0,ind):
               if arr[i]>=arr[i+1]:
                   return False
           for i in range(ind,len(arr)-1):
               if arr[i+1]>=arr[i]:
                   return False
           return True
    
       # if len(arr)<3:
       #     return False
       # m = max(arr)
       # ind = arr.index(m)
       # if ind==0 or ind==len(arr)-1:
       #     return False
       # for i in range(ind-1):
       #     if arr[i]>=arr[i+1]:
       #         return False
       # for i in range(ind,len(arr)-1):
       #     if arr[i]<=arr[i+1]:
       #         return False
       # return True
       # 