class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice = True

        while n >= stones:
            n = n - stones
            stones = stones - 1
            if alice:
                alice = False
            else:
                alice = True

        if alice:
            return False
        else:
            return True