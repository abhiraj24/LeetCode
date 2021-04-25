class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0
        i=0
        while(i < len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0):
                    count = count + 1
                    i = i + 1
            i = i + 1
        return count - n >= 0
        
        
        
##        ######naive#########
##        cnt=0
##        i=0
##        
##        if len(flowerbed)==1:
##            if flowerbed[0]==0:
##                cnt=1
##                if n<=cnt: 
##                    return True
##                else: 
##                    return False
##        
##        if len(flowerbed)==2:
##            if flowerbed[0]==0 and flowerbed[1]==0:
##                cnt=1
##                if n<=cnt: 
##                    return True
##                else: return False
##            
##        
##        if(flowerbed[0]==0 and flowerbed[1]==0 and flowerbed[2]==1):
##                    cnt+=1
##                    flowerbed[0]=1
##        if(flowerbed[0]==0 and flowerbed[1]==0 and flowerbed[2]==0):
##                    cnt+=1
##                    flowerbed[0]=1
##        
##            
##        while i <len(flowerbed)-1:
##            #if i+1< len(flowerbed):
##            if(flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]==0):
##                    cnt+=1
##                    flowerbed[i]=1
##                    i+=1
##            i+=1
##        
##        if(flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0 and flowerbed[len(flowerbed)-3]==1):
##                    cnt+=1
##                    flowerbed[len(flowerbed)-1]=1
##        
##        if n<=cnt:
##            return True
##        else:
##            return False