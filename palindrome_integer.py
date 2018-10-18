class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        a=str(A)
        if A<0:
            return 0
        elif a[::]==a[::-1]:
            return 1
        else:
            return 0
                