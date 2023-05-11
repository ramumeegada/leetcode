#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        a = N
        count = 0
        while N != 0:
            if N%10 != 0 and a%(N%10) == 0:
                count += 1
                N //= 10
            else:
                N //= 10
        return count        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends