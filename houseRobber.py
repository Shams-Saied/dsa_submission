class Solution(object):
    def rob(self, nums):
        mx1=0
        mx2=0

        for num in nums:
            temp=max(num+mx1,mx2)
            mx1=mx2
            mx2=temp
        return mx2

    
nums = [2,7,9,3,1]
sol=Solution()
print(sol.rob(nums))

        