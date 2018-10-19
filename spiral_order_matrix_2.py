class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        l = [[0] * A for i in range(A)]
        if A==0:
            return A
        n=1
        xStart=0
        yStart=0
        xEnd=A-1
        yEnd=A-1
        while n<=A*A:
            for i in range(yStart,yEnd+1):
                l[xStart][i]=n
                n+=1
            xStart+=1
            for i in range(xStart,xEnd+1):
                l[i][yEnd]=n
                n+=1
            yEnd-=1
            for i in range(yEnd,yStart-1,-1):
                l[xEnd][i]=n
                n+=1
            xEnd-=1
            for i in range(xEnd,xStart-1,-1):
                l[i][yStart]=n
                n+=1
            yStart+=1
        return l
            