## 🧠 Notes on LeetCode 1: Two Sum (Brute Force)
- It works fine for small inputs, but slow for large ones.
- Next step: try hash map method to reduce time complexity to O(n).
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []
