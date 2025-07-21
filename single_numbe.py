Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d=[]
        for i in nums:
            if nums.count(i)==1:
                s=i
        return s

    
