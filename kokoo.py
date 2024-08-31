import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        c=0
        sum=0
        mx=piles[0]
        s=mx

        for i in piles:
            sum+=i
            if(i>mx):
                mx=i

        mn=sum/h

        piles.sort()
        
        for j in range(int(mn),int(mx)):
            c=0
            for i in piles:
                if i<=j:
                    c=c+1
                else:
                    c=c+math.ceil(i/j)
            if c==h:
                s=j
                break
        return s
        
        


sol=Solution()
piles = [3,6,7,11]
h = 8

print(sol.minEatingSpeed(piles,h))