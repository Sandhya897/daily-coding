class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        d=[]
        for i in range(len(nums)):
            b=nums[i]*nums[i]
            d.append(b)
        d.sort()
        return d 
