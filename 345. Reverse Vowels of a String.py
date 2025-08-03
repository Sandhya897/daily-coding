class Solution:
    def reverseVowels(self, s: str) -> str:
        a=set("aeiouAEIOU")
        s=list(s)
        i=0
        j=len(s)-1
        while(i<j):
            if s[i] in a and s[j] in a:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
                i=i+1
                j=j-1
            elif s[i] not in a:
                i=i+1
            else:
                j=j-1
        return "".join(s)  
