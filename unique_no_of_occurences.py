'''unique no of occurrences'''
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=[]
        for i in set(arr):
            d.append(arr.count(i))
        if len(d)==len(set(d)):
            return True
        else:
            return False
