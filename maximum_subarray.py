class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cu=0
        max1=nums[0]
        for i in range(0,len(nums)):
            cu=cu+nums[i]
            max1=max(cu,max1)
            if cu<0:
                cu=0
        return max1
