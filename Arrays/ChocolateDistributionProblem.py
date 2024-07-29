class Solution:

    def findMinDiff(self, A,N,M):
        if M == 0 or N == 0:
            return 0
        A.sort()
        min1 = float('inf')
        for i in range(N-M+1):
            k = A[M+i-1] - A[i]
            min1 = min(min1,k)
        return min1