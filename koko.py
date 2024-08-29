class Solution(object):
    def minEatingSpeed(self, piles, h):
        sum=0
        for i in piles:
            sum+=i
        return sum/len(piles)