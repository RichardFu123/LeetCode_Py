class Solution:
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        def gcd(a,b):
            if a<b: return gcd(b,a)
            if b==0: return a
            return gcd(b,a%b)

        lo,hi,lcm = int(min(a,b)*n/2),min(a,b)*n,(a*b)//gcd(a,b)

        while lo<=hi:           
            mid=lo+(hi-lo)//2           
            res=mid//a+mid//b-mid//lcm
            if res==n: 
                break
            if res<n: 
                lo,hi=mid+1,hi
            else:
                lo,hi =lo,mid-1
                
        while mid%a and mid%b:
            mid-=1
        return mid % 1000000007
