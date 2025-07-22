//1002. Find Common Characters
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s=[list(k) for k in words]
        c=s[0]
        for i in s[1:]:
            temp=[]
            for j in c:
                if j in i:
                    temp.append(j)
                    i.remove(j)
            c=temp
        return c
