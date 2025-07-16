## Sliding Window Exploration  
Today I learned how to use two pointers to maintain a subarray of size k.  
I'm still confused when the window hits the end of the array. Need to recheck edge cases.
## Sliding Window: Max Subarray Sum
This Python code finds the  Minimum Size Subarray Sum

```python
 class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        m=float("inf")
        for i in range(len(nums)):
            s=s+nums[i]
            while s>=target:
                m=min(m,i-l+1)
                s=s-nums[l]
                l=l+1
        return m if m!=float("inf") else  0
