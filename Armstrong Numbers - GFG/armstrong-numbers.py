#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        res = 0
        a = n
        while n != 0:
            res += (n%10)**3
            n //= 10
        if res == a:
            return "Yes"
        return "No"    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends