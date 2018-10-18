class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        
        count=0
        i=1
        while (A)//(5**i)>=1:
            count+=(A)//(5**i)
            i+=1
        return count
                
            
    