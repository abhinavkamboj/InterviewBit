class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        n=len(A)
        alphabets={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        temp=0
        z=26
        ans=0
        for x in A[-1::-1]:
            ans+=(alphabets[x])*(z**temp)
            temp+=1
        return ans