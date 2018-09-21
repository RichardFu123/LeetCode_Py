class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.replace('i','j')
        b = b.replace('i','j')
        c = eval(a)*eval(b)
        return str(int(c.real))+"+"+str(int(c.imag))+"i"
