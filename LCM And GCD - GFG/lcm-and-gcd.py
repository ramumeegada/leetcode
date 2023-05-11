#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
            a,b = A,B
            while A%B != 0:
                A, B = B, A%B
            lcm = (a*b)/B
            return [int(lcm),B]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends