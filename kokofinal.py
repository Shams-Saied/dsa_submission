import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        
        l=1
        r =max(piles)

        while l < r:
            mid = (l+r) //2 
            
            count = 0
            for pile in piles:
                if pile<=mid:
                    count+=1
                elif pile%mid==0:
                    count+=pile//mid
                else:
                    count += (pile//mid+1)

            if count <= h:
                r = mid
            else:
                l = mid +1
        
        return l
    


sol=Solution()
piles = [3,6,7,11]
h = 8

print(sol.minEatingSpeed(piles,h))