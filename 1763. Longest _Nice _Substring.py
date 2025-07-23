'''longest Nice Substring'''
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        m=0
        r=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                c=s[i:j+1]
                d=True
                '''convert as set in substring why beacuse for fatser computations for multiole checking  l=set(c)'''
                for ch in c:
                     if ch.lower() not in c or ch.upper() not in c:
                        d=False 
                        break
                if d==True and len(c)>m:
                    m=len(c)
                    r =c
        return r
