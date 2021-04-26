class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0,y0=coordinates[0]
        x1,y1=coordinates[1]
        
        dy=y1-y0
        dx=x1-x0
        
        p=dx*y0-dy*x0
        
        for x,y in coordinates[2:]:
            if (dx*y-dy*x)!=p:
                return False
        return True

    