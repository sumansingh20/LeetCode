class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while True:
            x = num
            result = 1
            while x > 0:
                result *= x % 10
                x //= 10
            if result % t == 0:
                return num
            num += 1