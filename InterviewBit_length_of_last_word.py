class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLastWord(self, A):
	    index=0
	    count=0
	    if A=="":
	        return 0
	    for x in range(len(A)-1,-1,-1):
            if ord(A[x])!=32:
                index=x
                break
            else:
                continue
        
        for y in range(index,-1,-1):
            if ord(A[y])==32:
                break
            else:
                count+=1
        return count