class Solution:
	# @param A : integer
	# @return a list of list of integers
	def prettyPrint(self, A):
        r=2*A-1
        c=2*A-1
        l= [[0 for x in range(r)] for y in range(c)] 
        q=0
        w=r-1
        a=A
        for x in range(0,A):
            for y in range(q,w+1):
                l[q][y]=a
                l[y][q]=a
                l[w][y]=a
                l[y][w]=a
            a-=1
            q+=1
            w-=1
        return l