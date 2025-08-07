class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        five=int(0.05*n)
        mean=arr[five:n-five]
        s=sum(mean)
        return s/len(mean)
