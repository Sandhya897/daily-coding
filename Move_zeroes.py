class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos=0
        for i in nums:
            if i!=0:
                nums[pos]=i
                pos +=1
        for i in range(pos,len(nums)):
            nums[pos]=0
            pos=pos+1
        return nums
