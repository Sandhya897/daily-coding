
'''3090. Maximum Length Substring With Two Occurrences'''
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m=0
        
        for i in range(len(s)):
            for j in range(i,len(s)):
                c=s[i:j+1]
                d=True
                for k in c:
                    if c.count(k)<=2:
                        d=True     
                    else:
                        d=False
                        break
                if d==True:
                    m=max(m,len(c))
                
        return m
                
