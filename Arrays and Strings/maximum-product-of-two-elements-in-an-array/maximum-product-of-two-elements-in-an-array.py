class Solution:
    def maxProduct(self, nums: List[int]) -> int:
           l=[i-1 for i in nums]
           max_ele=l[0]
           
           for i in range(1,len(l)):
               if l[i]>max_ele:
                   max_ele=l[i]
           
           cnt=-1
           for i in range(0,len(l)):
               if l[i]==max_ele:
                   cnt+=1
                   
           if cnt>0: 
               return max_ele*max_ele
           
           m=[i for i in l if i!=max_ele]
           sec_ele=m[0]
           for i in range(1,len(m)):
               if m[i]>sec_ele:
                   sec_ele=m[i]
    
           return max_ele*sec_ele 
    
        #nums.sort()
        #return (nums[-1]-1)*(nums[-2]-1)
                