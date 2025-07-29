class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        d=0
        for i in range(len(s)-3+1):
            c=s[i:i+3]
            if len(set(c))==3:
                d=d+1
        return d
