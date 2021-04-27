class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        """
        cnt=len([val for val in arr if val==0])
        #cnt=len([val for val in arr if val==0])
        i=0
        while i<len(arr)-1:
            if arr[i]==0:
                arr[:]=arr[0:i+1]+[0]+arr[i+1:len(arr)-1]
                #print(i)
                #print(arr)
                cnt-=1
                i=i+2
            else:
                i=i+1
                
        #return arr
