class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, step = 1, 1, 9
        while n > size * step:
            n, size, step, start = n - (size * step), size + 1, step * 10, start * 10
        return int(str(start + (n - 1) // size)[(n - 1) % size])
