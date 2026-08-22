class Solution:
    def checkDivisibility(self, n: int) -> bool:
        x = n
        total = 0
        product = 1

        while x:
            digit = x % 10
            total += digit
            product *= digit
            x //= 10

        return n % (total + product) == 0